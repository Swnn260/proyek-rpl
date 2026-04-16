MAX_TOTAL = 50

def hitung_total(nilai, jumlah):
    """Menghitung total nilai, maksimal 50."""
    
    total = nilai * jumlah
    return min(total, MAX_TOTAL)
