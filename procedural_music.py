import sys
from PyQt5.QtWidgets
import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QMediaPlayer, QVideoWidget, QComboBox

class MusicPlayer(QMainWindow):
    def __init__(self, music_file):
    super().__init__()
self.initUI(music_file)

def initUI(self, music_file): #Create a QMediaPlayer and a QVideoWidget
self.player = QMediaPlayer(self)
self.video_widget = QVideoWidget(self)

# Set the QVideoWidget as the video output
for the QMediaPlayer
self.player.setVideoOutput(self.video_widget)


# Load the music file into the QMediaPlayer
self.player.setMedia(QMediaContent(QUrl.fromLocalFile(music_file)))

# Create buttons for controlling the music player
play_button = QPushButton('Play', self)
pause_button = QPushButton('Pause', self)
stop_button = QPushButton('Stop', self)

# Connect the buttons to the appropriate player methods
play_button.clicked.connect(self.player.play)
pause_button.clicked.connect(self.player.pause)
stop_button.clicked.connect(self.player.stop)


# Create buttons for modifying the volume and playback speed
volume_up_button = QPushButton('Volume Up', self)
volume_down_button = QPushButton('Volume Down', self)
speed_up_button = QPushButton('Speed Up', self)
speed_down_button = QPushButton('Speed Down', self)

# Connect the buttons to the appropriate player methods
volume_up_button.clicked.connect(self.volumeUp)
volume_down_button.clicked.connect(self.volumeDown)
speed_up_button.clicked.connect(self.speedUp)
speed_down_button.clicked.connect(self.speedDown)

# Create a horizontal layout for the volume buttons
volume_button_layout = QHBoxLayout()
volume_button_layout.addWidget(volume_up_button)
volume_button_layout.addWidget(volume_down_button)

# Create a horizontal layout for the speed buttons
speed_button_layout = QHBoxLayout()
speed_button_layout.addWidget(speed_up_button)
speed_button_layout.addWidget(speed_down_button)


# Create a combo box for selecting the atmosphere
atmosphere_combo_box = QComboBox(self)
atmosphere_combo_box.addItem('Relaxing')
atmosphere_combo_box.addItem('Energizing')
atmosphere_combo_box.addItem('Calming')

# Connect the combo box to the atmosphereChanged method
atmosphere_combo_box.activated[str].connect(self.atmosphereChanged)



# Create a vertical layout
for the video widget, buttons, and sliders
main_layout = QVBoxLayout()
main_layout.addWidget(self.video_widget)
main_layout.addLayout(button_layout)
main_layout.addWidget(atmosphere_combo_box) main_layout.addLayout(volume_button_layout)
main_layout.addLayout(speed_button_layout)

# Set the layout as the central widget
self.setCentralWidget(main_layout)

def atmosphereChanged(self, atmosphere): #Modify the music to match the selected atmosphere
def atmosphereChanged(self, atmosphere): #Modify the music to match the selected atmosphere
if atmosphere == 'Relaxing': #Set the volume and playback speed to relaxing values
self.player.setVolume(50)
self.player.setPlaybackRate(1.0)
elif atmosphere == 'Energizing': #Set the volume and playback speed to energizing values
self.player.setVolume(80)
self.player.setPlaybackRate(1.5)
elif atmosphere == 'Calming': #Set the volume and playback speed to calming values
self.player.setVolume(30)
self.player.setPlaybackRate(0.5)

def volumeUp(self): #Increase the volume by 10 %
    self.player.setVolume(self.player.volume() + 10)

def volumeDown(self): #Decrease the volume by 10 %
    self.player.setVolume(self.player.volume() - 10)

def speedUp(self): #Increase the playback speed by 10 %
    self.player.setPlaybackRate(self.player.playbackRate() + 0.1)

def speedDown(self): #Decrease the playback speed by 10 %
    self.player.setPlaybackRate(self.player.playbackRate() - 0.1)



# Create a horizontal layout for the buttons
button_layout = QHBoxLayout()
button_layout.addWidget(play_button)
button_layout.addWidget(pause_button)
button_layout.addWidget(stop_button)

# Create a vertical layout for the video widget and buttons
main_layout = QVBoxLayout()
main_layout.addWidget(self.video_widget)
main_layout.addLayout(button_layout)

# Set the layout as the central widget
self.setCentralWidget(main_layout)

# Create the PyQt5 application
app = QApplication(sys.argv)

# Create a MusicPlayer instance and show it
player = MusicPlayer('procedural_music.mp3')
player.show()

# Run the application
sys.exit(app.exec_())
