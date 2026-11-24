# FOSSBot – Symulacja i Interfejs Sterowania (ROS 2)

Instrukcja instalacji i uruchomienia modelu symulacyjnego robota mobilnego (**FOSSBotEduSim**) wraz z panelem sterowania oraz dashboardem podglądu (**fossbot_interface**) na czystym systemie Linux (Ubuntu WSL).

---

## 1. Wymagania systemowe

* **System operacyjny:** Linux Ubuntu 
* **Dostęp do internetu** oraz uprawnienia administratora (`sudo`).
* **Środowisko graficzne** wymagane do wyświetlenia symulacji oraz okien OpenCV.

---

## 2. Instalacja ROS 2 na czystym systemie Ubuntu

Jeśli masz już zainstalowany ROS 2, przejdź od razu do **Kroku 3**.

### 2.1. Ustawienie kodowania UTF-8
```bash
sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 2.2. Dodanie repozytorium ROS 2
```bash
sudo apt install -y software-properties-common curl git
sudo add-apt-repository universe -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 2.3. Instalacja ROS 2 Desktop oraz narzędzi budowania
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
  ros-lyrical-desktop \
  python3-colcon-common-extensions \
  python3-rosdep \
  python3-opencv \
  python3-numpy
```

### 2.4. Inicjalizacja `rosdep`
```bash
sudo rosdep init
rosdep update
```

---

## 3. Pobranie repozytoriów (model + sterowanie)

Utwórz wspólny workspace ROS 2 (`~/fossbot_ws`) i pobierz do niego oba repozytoria:

```bash
mkdir -p ~/fossbot_ws/src
cd ~/fossbot_ws/src
git clone https://github.com/LRMPUT/FOSSBotEduSim.git
git clone https://github.com/DOMPUR/fossbot_interface.git /tmp/git_temp
cp -r /tmp/git_temp/src/fossbot_interface ~/fossbot_ws/src/
rm -rf /tmp/git_temp
```

---

## 4. Instalacja zależności i budowanie projektu

Załaduj bazowe środowisko ROS 2, doinstaluj brakujące pakiety wymagane przez oba repozytoria i zbuduj cały workspace:

```bash
cd ~/fossbot_ws
source /opt/ros/lyrical/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
```

---

## 5. Trwała konfiguracja środowiska (automatyczne ładowanie)

```bash
echo "source /opt/ros/lyrical/setup.bash" >> ~/.bashrc
echo "source ~/fossbot_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## 6. Uruchamianie programu

Po wykonaniu powyższej instalacji, w każdym nowym terminalu — również po restarcie komputera — wystarczy uruchomić jedną komendę:

Domyślne ustawienia:
```bash
ros2 launch fossbot_interface fossbot.launch.py
```
Zmiana prędkości zadanej (np. vel = 0.3):
```bash
ros2 launch fossbot_interface fossbot.launch.py vel:=0.3
```


Polecenie uruchomi jednocześnie:
1. **Symulację i wizualizację robota** (`fossbot_educational_description`),
2. **Panel sterowania** (`FossBot - Panel Sterowania`),
3. **Podgląd telemetrii na żywo** (`FossBot - Dashboard na zywo`).

### Obsługa panelu sterowania
* **Lewy przycisk myszy (górna połowa okna):** jazda do przodu.
* **Lewy przycisk myszy (dolna połowa okna):** jazda do tyłu.
* **Prawy przycisk myszy:** zatrzymanie.
* **Zamknięcie programu:** naciśnij `Ctrl + C` w oknie terminala.

---
