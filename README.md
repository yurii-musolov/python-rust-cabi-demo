# Python + Rust (C ABI) Demo

Наглядный пример ускорения Python через вызов Rust-кода по C ABI.
В примере сравниваются две реализации вычисления суммы квадратов:
- чистый Python
- Rust через `ctypes` + C ABI

На больших числах Rust обычно работает значительно быстрее.

---

## Требования

- Python 3.11+
- Rust + Cargo
- just

---

## Быстрый старт

```bash
just demo
```

Команда:

1. соберёт Rust dynamic library
2. запустит benchmark Python vs Rust

---

## Ожидаемый вывод

```text
Python result: 333328333350000
Python time  : 0.0037 sec

Rust result: 333328333350000
Rust time  : 0.0000 sec

Rust is faster ~450.7x
```
