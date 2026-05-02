import time
import threading
import multiprocessing
import matplotlib.pyplot as plt


def kareler_toplami(n):
    toplam = 0
    for i in range(n):
        toplam += i * i
    return toplam


def thread_ile_calistir(n, kac_thread=4):
    threadler = []
    baslangic = time.time()
    for i in range(kac_thread):
        t = threading.Thread(target=kareler_toplami, args=(n,))
        threadler.append(t)
        t.start()
    for t in threadler:
        t.join()
    return time.time() - baslangic


def process_ile_calistir(n, kac_process=4):
    processler = []
    baslangic = time.time()
    for i in range(kac_process):
        p = multiprocessing.Process(target=kareler_toplami, args=(n,))
        processler.append(p)
        p.start()
    for p in processler:
        p.join()
    return time.time() - baslangic


if __name__ == "__main__":

    n_degerleri     = [100_000, 300_000, 500_000, 700_000, 1_000_000,
                       2_000_000, 3_000_000, 5_000_000, 7_000_000, 10_000_000]

    thread_sureleri  = []
    process_sureleri = []
    breakeven_n      = None

    print("=" * 60)
    print("Scenario 2: Searching for break-even point...")
    print("=" * 60)
    print(f"{'n Degeri':<15} {'Thread (s)':<15} {'Process (s)':<15} {'Winner'}")
    print("-" * 60)

    for n in n_degerleri:
        t_thread  = thread_ile_calistir(n)
        t_process = process_ile_calistir(n)

        thread_sureleri.append(t_thread)
        process_sureleri.append(t_process)

        if t_thread < t_process:
            kazanan = "Thread"
        else:
            kazanan = "PROCESS !!!"
            if breakeven_n is None:
                breakeven_n = n

        print(f"{n:<15,} {t_thread:<15.3f} {t_process:<15.3f} {kazanan}")

    print("=" * 60)
    if breakeven_n:
        print(f"\nBreak-even point: n = {breakeven_n:,}")

    x_etiketler = [f"{n/1_000_000:.1f}M" for n in n_degerleri]

    plt.figure(figsize=(10, 6))
    plt.plot(x_etiketler, thread_sureleri,
             marker='o', color='#2ecc71', linewidth=2, label='Threading')
    plt.plot(x_etiketler, process_sureleri,
             marker='s', color='#3498db', linewidth=2, label='Multiprocessing')

    if breakeven_n:
        idx = n_degerleri.index(breakeven_n)
        plt.axvline(x=idx, color='#e74c3c', linestyle='--',
                    linewidth=1.5, label=f'Break-even (n={breakeven_n/1_000_000:.1f}M)')

    plt.title('Scenario 2: Threading vs Multiprocessing (CPU-Bound)')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size (millions)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('senaryo2_grafik.png', dpi=150)
    plt.show()

    print("Grafik kaydedildi: senaryo2_grafik.png")