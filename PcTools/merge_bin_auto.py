# merge_bin.py
from pathlib import Path
import sys


def find_bin_files(root: Path, exclude: set = None):
    """递归搜索 root 下所有 .bin 文件，按相对路径排序，排除指定文件。"""
    exclude = exclude or set()
    files = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() != ".bin":
            continue
        # 用绝对路径比较，避免相对路径写法差异
        if p.resolve() in exclude:
            continue
        files.append(p)

    # 按相对路径小写排序，保证结果稳定、可复现
    files.sort(key=lambda p: str(p.relative_to(root)).lower())
    return files


def merge_bin_files(files, root: Path,
                    output_bin="all.bin",
                    output_txt="allname.txt",
                    ansi_encoding="gbk"):
    out_bin = root / output_bin
    out_txt = root / output_txt

    # 防止把输出文件自己合并进去
    exclude = {out_bin.resolve(), out_txt.resolve()}
    valid_files = [p for p in files if p.resolve() not in exclude]

    if not valid_files:
        print("未找到任何可合并的 .bin 文件。")
        return

    with out_bin.open("wb") as fb, out_txt.open("wb") as ft:
        for p in valid_files:
            # 直接追加 bin 内容，中间不加任何分隔
            with p.open("rb") as fin:
                while True:
                    chunk = fin.read(1024 * 1024)  # 每次读 1MB
                    if not chunk:
                        break
                    fb.write(chunk)

            # 文件名去掉 .bin 后缀
            name_without_ext = p.stem

            # ANSI（中文 Windows 下一般为 GBK）编码
            try:
                data = name_without_ext.encode(ansi_encoding)
            except UnicodeEncodeError:
                print(f"警告：文件名 '{name_without_ext}' 无法用 {ansi_encoding} 编码，已替换无法表示的字符。")
                data = name_without_ext.encode(ansi_encoding, errors="replace")

            # 每个文件名后使用 \r\n 换行
            ft.write(data + b"\r\n")

    print(f"合并完成，共 {len(valid_files)} 个 bin 文件：")
    for p in valid_files:
        print(f"  {p.relative_to(root)}")
    print(f"\n输出文件: {out_bin}")
    print(f"文件名列表: {out_txt}（编码: {ansi_encoding}）")


def main():
    # 搜索根目录：默认脚本所在目录
    if len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()
    else:
        root = Path(__file__).resolve().parent

    if not root.is_dir():
        print(f"错误：目录不存在 {root}")
        return

    print(f"搜索目录: {root}")
    files = find_bin_files(root, exclude={
        (root / "all.bin").resolve(),
    })

    merge_bin_files(files, root)


if __name__ == "__main__":
    main()