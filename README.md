# LaTeX Vietnamese–Japanese–English Book Template

Template soạn **sách đa ngôn ngữ Việt – Nhật – English** bằng **LuaLaTeX**.  
Thiết kế hướng tới **sách dài, tài liệu học tập và xuất bản PDF chất lượng cao**.

---

## Tính năng

Hỗ trợ:
- Unicode tiếng Việt đầy đủ
- Tiếng Anh (Latin)
- Tiếng Nhật (CJK) với **furigana trên đầu kanji**
- Xuất PDF chất lượng in ấn
- Font tối ưu cho đọc lâu
- Viết nội dung **trực tiếp**, không cần environment riêng cho ngôn ngữ
- Cấu hình ổn định, dễ bảo trì cho sách lớn

---

## Yêu cầu hệ thống

- TeX Live (khuyến nghị bản đầy đủ)
- Trình biên dịch: **LuaLaTeX**

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install \
  texlive-full \
  fonts-libertinus \
  fonts-noto \
  fonts-noto-cjk
```

### Windows / macOS

- Cài TeX Live: https://tug.org/texlive/
- Font Libertinus: https://github.com/libertinus-fonts/libertinus
- Font Nhật: Noto Serif CJK (đi kèm TeX Live hoặc Google Fonts)

---

## Cấu trúc thư mục

```text
book/
 ├─ main.tex
 ├─ chapters/
 │   ├─ chap01.tex
 │   └─ chap02.tex
```

---

## Biên dịch

Trong thư mục `book/` chạy:

```bash
lualatex main.tex
lualatex main.tex
```

Chạy 2 lần để cập nhật mục lục, header và bookmark PDF.

Kết quả:

```text
main.pdf
```

---

## Viết nội dung đa ngôn ngữ

Ví dụ trong chương:

```tex
\chapter{Giới thiệu}

Đây là nội dung tiếng Việt.

\ruby{日本語}{にほんご}を\ruby{勉強}{べんきょう}しています。

This is an English sentence.
```

Quy ước:
- Tiếng Việt: chữ thường
- Tiếng Nhật: viết trực tiếp, dùng `\ruby{漢字}{かな}` cho furigana
- English: viết trực tiếp (có thể in nghiêng nếu muốn)

---

## Furigana (Ruby)

Cú pháp chuẩn:

```tex
\ruby{漢字}{かな}
```

Ví dụ:

```tex
\ruby{最後}{さいご}まで\ruby{読}{よ}んでいただき、ありがとうございました。
```

- Furigana hiển thị **trên đầu kanji**
- Chuẩn sách tiếng Nhật
- Không vỡ dòng, không lệch layout

---

## Thêm chương mới

Tạo file:

```text
chapters/chap03.tex
```

Thêm vào `main.tex`:

```tex
\include{chapters/chap03}
```

---

## Font đang dùng

- Nội dung chính: Libertinus Serif
- Sans: Libertinus Sans
- Mono: Libertinus Mono
- Japanese (CJK): Noto Serif CJK JP

---

## Trình soạn thảo đề xuất

- VS Code + LaTeX Workshop
- Engine: **LuaLaTeX**

---

## Lỗi thường gặp

### Sai engine

Chỉ dùng:

```bash
lualatex main.tex
```

Không dùng:

```bash
xelatex
pdflatex
```

---

### Thiếu font (Ubuntu)

```bash
sudo apt install fonts-libertinus fonts-noto fonts-noto-cjk
```

---

## Giấy phép

Tự do sử dụng cho mục đích cá nhân và thương mại.
