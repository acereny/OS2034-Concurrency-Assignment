import time
import threading
import multiprocessing
import matplotlib.pyplot as plt

NUM_TASKS = 50

def gorev(sayac, kilit):
    time.sleep(0.1)
    with kilit:
        sayac[0] += 1


def sirali_calistir():
    sayac = [0]
    kilit = threading.Lock()

    baslangic = time.time()

    for i in range(NUM_TASKS):
        gorev(sayac, kilit)

    sure = time.time() - baslangic

    print(f"Sequential    -> Time: {sure:.2f}s  |  Completed: {sayac[0]}")
    return sure

def threadli_calistir():
    sayac = [0]
    kilit = threading.Lock()

    baslangic = time.time()

    thread_listesi = []

    for i in range(NUM_TASKS):
        t = threading.Thread(target=gorev, args=(sayac, kilit))
        thread_listesi.append(t)
        t.start()


    for t in thread_listesi:
        t.join()

    sure = time.time() - baslangic

    print(f"Threading   -> Time: {sure:.2f}s  |  Completed: {sayac[0]}")
    return sure


def processli_calistir():
    sayac = multiprocessing.Value('i', 0)
    kilit = multiprocessing.Lock()

    baslangic = time.time()

    process_listesi = []

    for i in range(NUM_TASKS):
        p = multiprocessing.Process(target=process_gorevi, args=(sayac, kilit))
        process_listesi.append(p)
        p.start()

    for p in process_listesi:
        p.join()

    sure = time.time() - baslangic

    print(f"Processing  -> Time: {sure:.2f}s  |  Completed: {sayac.value}")
    return sure

def process_gorevi(sayac, kilit):
    time.sleep(0.1)
    with kilit:
        sayac.value += 1


if __name__ == "__main__":

    print("=" * 45)
    print("Scenario 1: Execution Time Analysis for 50 I/O Tasks")
    print("=" * 45)

    t1 = sirali_calistir()
    t2 = threadli_calistir()
    t3 = processli_calistir()

    print()
    print("--- Efficiency Analysis---")
    print(f"-Threading, {t1/t2:.1f} times faster than Sequential execution.")
    print(f"-Processing, {t1/t3:.1f} times faster than Sequential execution.")
    print(f"-Threading was {t3/t2:.1f} times faster than Processing execution.")

    yontemler = ['Sequential', 'Threading', 'Multiprocessing']
    sureler = [t1, t2, t3]
    renkler = ['#e74c3c', '#2ecc71', '#3498db']

    plt.figure(figsize=(8, 5))
    bars = plt.bar(yontemler, sureler, color=renkler, width=0.5)

    for bar, sure in zip(bars, sureler):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            f'{sure:.2f}s',
            ha='center', fontsize=11, fontweight='bold'
        )

    plt.title('Scenario 1: Execution Time Comparison (50 I/O Tasks)')
    plt.ylabel('Time (seconds)')
    plt.xlabel('Method')
    plt.ylim(0, max(sureler) * 1.2)
    plt.tight_layout()
    plt.savefig('senaryo1_grafik.png', dpi=150)
    plt.show()

    print("Grafik kaydedildi: senaryo1_grafik.png")