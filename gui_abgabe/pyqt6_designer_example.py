import sys
import numpy as np
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image
import pathlib
from matplotlib import pyplot as plt
import time
from PIL.PngImagePlugin import PngInfo
from datetime import datetime


def display_timestamp():
    """
    Das Format wird geändert. 'timestamp' kommt von der built in Funktion from datetime import datetime
    Args:
        timestamp: "2022-11-19 12:18:08.190088"

    Returns: "19. November 2022 12:18:08"
    """
    timestamp_now = str(datetime.now())
    timestamp = datetime.strptime(timestamp_now, "%Y-%m-%d %H:%M:%S.%f")
    eigenes_format = timestamp.strftime("%d. %B %Y %H:%M:%S")
    return eigenes_format


class MainWindow(QMainWindow):
    def __init__(self):
        # Welches Startbild?
        self.timestamp_now = 'None'

        file_name = 'mandelbrot_start_img_800.png'
        # file_name = 'mandelbrot_1_zoom_faktor_1.2.png'
        # file_name = 'cat_1.png'

        super().__init__()
        # creating label for filling the img in it
        self.label = QLabel(self)
        # Mit progress-bar
        uic.loadUi("gui_data_progress_bar_qlabel.ui", self)
        self.setMouseTracking(True)

        # get the img into the label
        path_to_img_src_folder = (pathlib.Path(__file__).parent.absolute()) / 'img_src'
        self.abs_filepath_start_img = path_to_img_src_folder / file_name
        print(f'abs file path start-image: \n{self.abs_filepath_start_img}')

        # Das Startbild wird in das GUI geladen
        self.load_img_into_label()

        # Variabel
        self.resetValue = False
        self.flag_img_saved = False
        self.image_counter = 0
        self.image_counter_for_gui_saving = 1
        self.value_zoom = 1.2
        # Mandelbrot params
        self.x1, self.y1, self.x2, self.y2 = -2, -2, 2, 2

        # Widgets from MainWIndow
        # Wenn der 'pushButton' geklickt wird
        self.pushButton.clicked.connect(self.handleButtonClick)
        self.setWindowTitle("Mandelbrot Zoom")
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon

        # External windows
        self.dialogWindow = DialogWindow()
        self.dialogWindow.yes_pushButton.clicked.connect(self.handleClickYes)
        self.dialogWindow.no_pushButton.clicked.connect(self.handleClickNo)
        self.show()

        # zoom_faktor
        self.zoom_faktor_einstellen.setValue(1.2)
        self.zoom_faktor_einstellen.setMaximum(4)
        self.zoom_faktor_einstellen.setMinimum(1.2)
        self.zoom_faktor_einstellen.setSingleStep(0.1)
        self.zoom_faktor_einstellen.valueChanged.connect(self.update_zoom_var)

        # tooltips
        self.zoom_faktor_einstellen.setToolTip('Zoomfaktor einstellen')
        self.pushButton.setToolTip('reset des Zommfaktor')
        self.label.setToolTip('Bild des Mandelbrot')
        self.progressBar.setToolTip('Fortschritt der Berechnung')

        # actionSave_as_png
        self.actionSave_as_png.triggered.connect(self.saving_img)
        self.actionquit.triggered.connect(self.close)

    def update_zoom_var(self):
        # global zoom_faktor
        self.value_zoom = self.zoom_faktor_einstellen.value()
        self.value_zoom = round(self.value_zoom, 1)

    # """
    # Close the application and check if the image is already saved otherwise show window with opportunity to save
    def closeEvent(self, event):
        if not self.flag_img_saved:  # when image isn't saved
            print('ich muss noch speichern')
            reply = QMessageBox.question(
                self, "Message",
                "Are you sure you want to quit? Any unsaved work will be lost.",
                QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
                QMessageBox.Save)
            if reply == QMessageBox.Close:
                quit()

            if reply == QMessageBox.Save:
                print("Bild im closeEvent gespeichert")
                self.saving_img()
            else:
                event.ignore()
                print('event ignore')

        else:  # when image is saved
            print("ich habe schon gespeichert")
            reply = QMessageBox.question(
                self, "Message",
                "Are you sure you want to quit? Any unsaved work will be lost.",
                QMessageBox.Close | QMessageBox.Cancel)
            if reply == QMessageBox.Close:
                quit()
            else:
                event.ignore()
            # """

    # reset zoomfaktor window when clicked yes
    def handleClickYes(self):
        self.resetValue = True
        self.dialogWindow.close()

    # reset zoomfaktor window when clicked no
    def handleClickNo(self):
        self.resetValue = False
        self.dialogWindow.close()

    # set zoomfaktor back to start value
    def handleButtonClick(self):
        self.dialogWindow.exec()
        if self.resetValue:
            self.zoom_faktor_einstellen.setValue(1.2)
            self.resetValue = False

    def load_img_into_label(self):
        global img_original_width, img_original_height
        # Originalgrösse vom Bild speichern
        with Image.open(self.abs_filepath_start_img) as img:
            img_original_width, img_original_height = img.size
            print('Image size():')
            print(f'original img x: {img_original_width}')
            print(f'original img y: {img_original_height}')

        # loading image
        self.label.setPixmap(QPixmap(str(self.abs_filepath_start_img)))
        # Offset y = 38 px
        # Offset x = 0 px
        self.label.setScaledContents(True)
        self.update()
        self.show()

    def mouseDoubleClickEvent(self, event):
        """
        Gibt die Koordinaten von dem Mauszeiger zurück, wennn man Doppel-Klickt
        """
        # Grössse vom Bild
        img_abs_size = self.label.size()
        img_abs_size_x = img_abs_size.width()
        img_abs_size_y = img_abs_size.height()

        # Koordinaten vom aktuellen Doppelklick
        local_coor = event.pos()
        local_coor_x = local_coor.x()
        local_coor_y = local_coor.y()

        # print(f'global_x: {img_original_width}')
        # print(f'global_y: {img_original_height}')

        # berechnet die absoluten Koordinaten vom Bild
        if local_coor_x <= img_abs_size_x and local_coor_y <= (img_abs_size_y + 38):
            # print('drinnen')
            # print(f'abs: {img_abs_size}')
            # print(f'lokal: {local_coor}')
            # Berechnung vom geklickten Punkt relativ
            ratio_x = img_abs_size_x / img_original_width
            ratio_y = img_abs_size_y / img_original_height

            point_now_abs_x = img_abs_size_x - local_coor_x
            point_now_abs_y = img_abs_size_y - local_coor_y

            self.point_rel_x = img_original_width - (int(point_now_abs_x / ratio_x))
            self.point_rel_y = img_original_height - (int(point_now_abs_y / ratio_y))

            # print(f'point_rel_x: {self.point_rel_x}')
            # print(f'point_rel_y: {self.point_rel_y}')

            # Geklickte Koordinaten umwandeln in Mandelbrot Koordinaten
            self.mandelbrot_parameter()

            # reset flag, weil das aktuelle Bild noch nicht gespeichert ist!
            self.flag_img_saved = False

            # TODO: progress bar!!
            # Das Mandelbrot img wird berechnet
            self.run()
            # Das berechnete Bild wird gespeichert
            self.save_calculated_image()
            print('fertig')

            # Update the mandelbrot img im GUI
            self.load_new_mandelbrot_img()
            print(f'Aktueller Bild-Counter --> {self.image_counter}')

        else:
            print('Nicht im Bild!')

    def load_new_mandelbrot_img(self):
        """
        Updating the Mandelbrot-Image in the GUI
        """
        # loading image
        self.label.setPixmap(QPixmap(str(self.new_path_to_save_img)))
        # Offset y = 38 px
        # Offset x = 0 px
        self.label.setScaledContents(True)
        self.update()
        self.show()

    def mandelbrot_parameter(self):
        """
        Hier werden die geklickten Koordinaten in Mandelbrot koordinaten umgewandelt
        """
        # Mandelbrot koordinaten, bez. Bereiche berechnen
        self.maxiter = 500
        self.image_size = img_original_width
        # Geklickte koordinaten im GUI-Bild
        x = self.point_rel_x
        y = self.point_rel_y
        # Berechnung für Mandelbrot Koordinaten [-2, 2]
        x1_new = self.x1 + x / self.image_size * (self.x2 - self.x1) - (self.x2 - self.x1) / 2.0 / self.value_zoom
        x2_new = self.x1 + x / self.image_size * (self.x2 - self.x1) + (self.x2 - self.x1) / 2.0 / self.value_zoom
        y1_new = self.y1 + y / self.image_size * (self.y2 - self.y1) - (self.y2 - self.y1) / 2.0 / self.value_zoom
        y2_new = self.y1 + y / self.image_size * (self.y2 - self.y1) + (self.y2 - self.y1) / 2.0 / self.value_zoom
        self.x1 = x1_new
        self.x2 = x2_new
        self.y1 = y1_new
        self.y2 = y2_new

        print()
        print(f'Mandelbrot params @:')
        print(f'\tzoom_faktor: {self.value_zoom}')
        print(f'\tMandelbrot_x: {self.x1} to {self.x2}')
        print(f'\tMandelbrot_y: {self.y1} to {self.y2}')
        print('Start Mandelbrot calc')

    def mandelbrot_maxiter(self, c, maxiter):
        """
        vom Mandelbrot (Moodle)
        """
        z = 0
        for n in range(maxiter):
            if abs(z) > 2:
                return n
            z = z * z + c
        return maxiter

    def smooth_color(self, n, maxiter):
        """
        vom Mandelbrot (Moodle)
        """
        t = (1.0 * n) / maxiter
        return np.array([
            8.5 * (1 - t) * (1 - t) * (1 - t) * t,
            15 * (1 - t) * (1 - t) * t * t,
            9 * (1 - t) * t * t * t,
        ])

    def run(self):
        """
        Die Mandelbrot-Berechnung findet hier statt (linspace).
        Am schluss kommt das berechnete Mandelbrot image heraus --> self.calc_mandelbrot_image
        """
        tic = time.time()
        self.calc_mandelbrot_image = np.zeros((self.image_size, self.image_size, 3))
        real = np.linspace(self.x1, self.x2, self.calc_mandelbrot_image.shape[1])
        imag = np.linspace(self.y1, self.y2, self.calc_mandelbrot_image.shape[0])

        for col, re in enumerate(real):
            for row, im in enumerate(imag):
                n = self.mandelbrot_maxiter(complex(re, im), self.maxiter)
                self.calc_mandelbrot_image[row, col, :] = self.smooth_color(n, self.maxiter)

        tac = time.time()
        self.calculation_time = (tac - tic)
        print(f'took: {self.calculation_time} s')

    def save_calculated_image(self):
        """
        Das berechnete neue Mandelbrot Bild wird mit Hilfe der Matplotlib dargestellt.
        Mit Savefig() wird das Bild auch gespeichert, im 'img_src' Ordner
        """
        # Create Path to save img
        self.image_counter += 1
        # Neuer Name fürs Bild
        image_name = "mandelbrot_{}_zoom_faktor_{}.png".format(self.image_counter, self.value_zoom)
        print(f'image_name: {image_name}')
        # get the current path
        path = (pathlib.Path(__file__).parent.absolute())
        # Neuer absoluter Pfad inkl file-name wird erstellt
        self.new_path_to_save_img = path.parent / 'gui_abgabe' / 'autosaved_img' / image_name
        # print(f'path: {path}')
        # print(f'abs path: {new_path_to_save_img}')
        print()

        # Set the img-parameters
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        ax.imshow(self.calc_mandelbrot_image, interpolation="bicubic")
        ax.set_xticks([])
        ax.set_yticks([])
        # Save figure into folder --> 129 dpi = 800x800
        fig.savefig(str(self.new_path_to_save_img), bbox_inches="tight", pad_inches=-1, dpi=200)


        tic = time.time()
        # Save the metadata
        im1 = Image.open(self.new_path_to_save_img)
        self.timestamp_now = display_timestamp()
        try:
            metadata = PngInfo()
            metadata.add_text("timestamp", self.timestamp_now)
            metadata.add_text("image_counter", str(self.image_counter))
            metadata.add_text("counter_gui_saved", str(self.image_counter_for_gui_saving))
            metadata.add_text("calculation time [s]", str(self.calculation_time))
            metadata.add_text("zoom_faktor", str(self.value_zoom))
            metadata.add_text("Mandelbrot_x_min", str(self.x1))
            metadata.add_text("Mandelbrot_x_max", str(self.x2))
            metadata.add_text("Mandelbrot_y_min", str(self.y1))
            metadata.add_text("Mandelbrot_y_max", str(self.y2))

        except:
            metadata.add_text("timestamp", self.timestamp_now)
        # Bild speichern
        im1.save(self.new_path_to_save_img, pnginfo=metadata)
        # Get time
        tac = time.time()
        factor = (tac - tic)
        print(f'saving metadata took: {factor} s')









    def saving_img(self):
        """
        Bild speichern, wenn im Gui ausgewählt wird.
        Dazu wird ein eigener Ordner erstellt 'saved_images_by_gui'
        """
        image_name_to_save = ' '
        abs_path_current_mandelbrot = ' '

        # get counter
        print()
        print(f'image_counter now: {self.image_counter}')
        if self.image_counter == 0:
            print('Startbild saving')
            image_name_to_save = "mandelbrot_{}.png".format(self.image_counter_for_gui_saving)
            print(f'image_name: {image_name_to_save}')
            # get current img:
            abs_path_current_mandelbrot = self.abs_filepath_start_img

        elif self.image_counter > 0:
            print(f'Anzahl Gedrückte Events: {self.image_counter_for_gui_saving}')
            image_name_to_save = "mandelbrot_{}.png".format(self.image_counter_for_gui_saving)
            print(f'image_name: {image_name_to_save}')
            # get current img:
            abs_path_current_mandelbrot = self.new_path_to_save_img
        else:
            print('Fehler')

        # get the current path
        path = (pathlib.Path(__file__).parent.absolute())
        # go one level back and change to Mandelbrot
        abs_new_path_to_final_folder = path.parent / 'gui_abgabe' / 'saved_images_by_gui' / image_name_to_save
        print(f'abs path to save file: {abs_new_path_to_final_folder}')
        print(f'abs path to load file: {abs_path_current_mandelbrot}')

        # Counter heraufzählen!
        self.image_counter_for_gui_saving += 1
        # saving img

        im1 = Image.open(abs_path_current_mandelbrot)
        # Save the metadata
        self.timestamp_now = display_timestamp()
        try:
            metadata = PngInfo()
            metadata.add_text("timestamp", self.timestamp_now)
            metadata.add_text("image_counter", str(self.image_counter))
            metadata.add_text("counter_gui_saved", str(self.image_counter_for_gui_saving))
            metadata.add_text("calculation time [s]", str(self.calculation_time))
            metadata.add_text("zoom_faktor", str(self.value_zoom))
            metadata.add_text("Mandelbrot_x_min", str(self.x1))
            metadata.add_text("Mandelbrot_x_max", str(self.x2))
            metadata.add_text("Mandelbrot_y_min", str(self.y1))
            metadata.add_text("Mandelbrot_y_max", str(self.y2))
        except:
            metadata.add_text("timestamp", self.timestamp_now)

        # Bild speichern
        im1.save(abs_new_path_to_final_folder, pnginfo=metadata)

        # Set the flag to true, muss bei jeder neuen Berechnung auf False gesetzt werden!!
        self.flag_img_saved = True


class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon
        # uic.loadUi("gui_data.ui", self)
        # self.pushButton.clicked.connect(self.close)


if __name__ == "__main__":
    app_2 = QApplication(sys.argv)
    window = MainWindow()
    app_2.exec()
