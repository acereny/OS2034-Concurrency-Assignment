

OS 2034 – Operating Systems Assignment  
Computer Engineering, 2nd Year



This project compares three ways to run tasks in Python: sequential, multi-threading, and multi-processing. The goal is to find the break-even point where multiprocessing becomes faster than threading for CPU-bound tasks.


**Scenario 1 – I/O Simulation**  
50 tasks, each sleeping for 0.1 seconds to simulate I/O. Compared execution times across all three methods.
-----------------------------------
 |  Method        |      Time   |
----------------------------------
|Sequential           ->  5.03s |
----------------------------------
|Threading (5)        ->  0.12s |
----------------------------------
|Multiprocessing (5)  -> 6.08s  |
----------------------------------

Threading was the fastest. Multiprocessing was even slower than sequential because spawning 50 processes on Windows has too much overhead for short tasks.



**Scenario 2 – Break-Even Point**  
Ran a sum of squares calculation with increasing list sizes to find where multiprocessing beats threading.

- Break-even point on my machine: **n = 7,000,000**
- Below this, threading is faster
- Above this, multiprocessing pulls ahead because GIL becomes the bottleneck



```
senaryo1_basit.py       # Scenario 1 code
senaryo2_breakeven.py   # Scenario 2 code
senaryo1_grafik.png     # Scenario 1 chart
senaryo2_grafik.png     # Scenario 2 chart
report.pdf              # Full report
```

---

- CPU: Intel Core i5-12450H (8 cores)
- RAM: 7.7 GB
- OS: Windows 11

---


Aslı Ceren Yılmaz
Computer Engineering, 2nd Year
