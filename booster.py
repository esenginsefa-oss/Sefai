import subprocess
import time

def adb(cmd):
    subprocess.run(f"adb shell {cmd}", shell=True)

def oyun_modu_ac():
    print("[+] Oyun modu açılıyor...")
    
    # Animasyonları kapat
    adb("settings put global window_animation_scale 0.0")
    adb("settings put global transition_animation_scale 0.0")
    adb("settings put global animator_duration_scale 0.0")
    
    # GPU optimize
    adb("setprop debug.hwui.renderer skiagl")
    adb("setprop debug.performance.tuning 1")
    
    # Arkaplanı temizle
    adb("am kill-all")
    
    print("[+] Oyun modu aktif!")

def oyun_modu_kapat():
    print("[+] Normal moda dönülüyor...")
    
    adb("settings put global window_animation_scale 1.0")
    adb("settings put global transition_animation_scale 1.0")
    adb("settings put global animator_duration_scale 1.0")
    
    adb("setprop debug.hwui.renderer default")
    adb("setprop debug.performance.tuning 0")
    
    print("[+] Normal mod aktif!")

if __name__ == "__main__":
    secim = input("1: Oyun Modu Aç\n2: Kapat\nSeçim: ")
    if secim == "1":
        oyun_modu_ac()
    elif secim == "2":
        oyun_modu_kapat()

