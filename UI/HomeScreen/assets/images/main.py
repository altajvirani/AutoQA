from kivy.app import App
import time
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.animation import Animation
from kivy.metrics import dp
from bot import chat
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
import pyttsx3
import threading

KV = '''
#:import RGBA kivy.utils.rgba
<ImageButton@ButtonBehavior+Image>:
    size_hint: None, None
    size: self.texture_size
    canvas.before:
        PushMatrix
        Scale:
            origin: self.center
            x: .75 if self.state == 'down' else 1
            y: .75 if self.state == 'down' else 1
    canvas.after:
        PopMatrix
     
BoxLayout:
    orientation: 'vertical'
    MDFloatLayout:
        orientation: 'vertical'
        FitImage: 
            size_hint_y: 1.25
            allow_stretch: True
            source: "images/box1.png"
            pos_hint: {"x": 0, "top": 1}
            padding: [0,15]
        FitImage: 
            size_hint_y: None
            allow_stretch: True
            width: dp(120)
            height: dp(120)
            source: "images/box2.png"
            pos_hint: {"x": 0, "bottom": 1}
            padding: [0,-36]
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.725
            padding: [0,-1.25]
            pos_hint: { 'top' : .985, 'right': 0.995}
            MDBoxLayout:
                orientation: 'horizontal'
                MDIconButton:
                    title: "Back"
                    icon: "images/back.png"
                    on_press: app.image_press()
                MDIconButton:
                    icon: "images/botdp.png"
                    padding: [2,0]
                    halign: "left"
                    valign: "center"
                    on_press: app.on_bot_image_press()
                MDBoxLayout:
                    orientation: 'vertical'
                    valign: "center"
                    padding: [5,4]
                    MDLabel:
                        title: "Back"
                        text: "AutoQA AI"
                        font_size: '15sp'
                        font_name: 'fonts/helvetica/roundedbold.otf'
                        halign: "left"
                        valign: "bottom"
                        padding: [4,0]
                    MDLabel:
                        title: "Online"
                        text: "Online"
                        font_size: '12sp'
                        font_name: 'fonts/helvetica/regular.ttf'
                        halign: "left"
                        valign: "top"
                        padding: [4, 0]
                MDIconButton:
                    id: menu
                    icon: "images/menu.png"                  
    BoxLayout: 
        orientation: 'vertical'
        size_hint_y: 8.8
        RecycleView:
            id: rv
            data: app.messages
            viewclass: 'Message'
            do_scroll_x: False
            RecycleBoxLayout:
                id: box
                orientation: 'vertical'
                size_hint_y: None
                size: self.minimum_size
                default_size_hint: 1, None
                # magic value for the default height of the message
                default_size: 0, 38
                key_size: '_size'
        FloatLayout:
            size_hint_y: None
            height: 0
            Button:
                size_hint_y: None
                height: self.texture_size[1]
                opacity: 0 if not self.height else 1
                text:
                    (
                    'go to last message'
                    if rv.height < box.height and rv.scroll_y > 0 else
                    ''
                    )
                pos_hint: {'pos': (0, 0)}
                on_release: app.scroll_bottom()
                
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, 0.925
        size: self.minimum_size
        padding: [20, 0]
        MDTextField:
            id: ti
            allow_stretch: True
            multiline: False
            on_text_validate:
                app.send_message(self)
        MDIconButton:
            icon: 'images/send.png'
            pos_hint: {"top" : 0.925}
            on_release:
                app.send_message(ti)
<Message@FloatLayout>:
    message_id: -1
    bg_color: '#223344'
    side: 'left'
    text: ''
    size_hint_y: None
    _size: 0, 0
    size: self._size
    text_size: None, None
    opacity: min(1, self._size[0])
    Label:
        text: root.text
        padding: 10, 10
        size_hint: None, 1
        size: self.texture_size
        text_size: root.text_size
        on_texture_size:
            app.update_message_size(
            root.message_id,
            self.texture_size,
            root.width,
            )
        pos_hint:
            (
            {'x': 0, 'center_y': .5}
            if root.side == 'left' else
            {'right': 1, 'center_y': .5}
            )
        canvas.before:
            Color:
                rgba: RGBA(root.bg_color)
            RoundedRectangle:
                size: self.texture_size
                radius: dp(10), dp(10), dp(10), dp(10)
                pos: self.pos
        canvas.after:
            Color:
            Line:
                rounded_rectangle: self.pos + self.texture_size + [dp(5)]
                width: 1.01
'''
UI = '''
MDBoxLayout:
    orientation: 'vertical'
    MDScreen:
        MDRectangleFlatButton:
            text: "ALERT POPUP!"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_alert_dialog()
        MDLabel:
            id: my_label
            text: "Some Stuff"
            pos_hint: {'center_x': .95, 'center_y': .4}
            '''
Window.size = (393,700)
class MessengerApp(MDApp):
    messages = ListProperty()
    dialog = None
    dialogBot = None

    def build(self):
        self.title = 'Natural Language Processing'
        return Builder.load_string(KV)

    def add_message(self, text, side, color):
        # create a message for the recycleview
        self.messages.append({
            'message_id': len(self.messages),
            'text': text,
            'side': side,
            'bg_color': color,
            'text_size': [None, None],
        })

    def add_message(self, text, side, color):
        # create a message for the recycleview
        self.messages.append({
            'message_id': len(self.messages),
            'text': text,
            'side': side,
            'bg_color': color,
            'text_size': [None, None],
        })

    def update_message_size(self, message_id, texture_size, max_width):
        # when the label is updated, we want to make sure the displayed size is
        # proper
        if max_width == 0:
            return

        one_line = dp(50)  # a bit of  hack, YMMV

        # if the texture is too big, limit its size
        if texture_size[0] >= max_width * 2 / 3:
            self.messages[message_id] = {
                **self.messages[message_id],
                'text_size': (max_width * 2 / 3, None),
            }

        # if it was limited, but is now too small to be limited, raise the limit
        elif texture_size[0] < max_width * 2 / 3 and \
                texture_size[1] > one_line:
            self.messages[message_id] = {
                **self.messages[message_id],
                'text_size': (max_width * 2 / 3, None),
                '_size': texture_size,
            }

        # just set the size
        else:
            self.messages[message_id] = {
                **self.messages[message_id],
                '_size': texture_size,
            }




    def send_message(self, textinput):
        text = textinput.text
        textinput.text = ''
        if len(text) != 0:
            self.add_message(text, 'right', '#223344')
            self.focus_textinput(textinput)
            ob = chat(text)
            Clock.schedule_once(lambda *args: self.answer(ob), 1)
            self.scroll_bottom()

        else:
            message = 'Please enter Your Question!'
            toast( 'Please enter Your Question!' )
            time.sleep( 0 )
            t2 = threading.Thread( target=self.playResponce, args=(message,) )
            t2.start()


    def answer(self, ob, *args):
        self.add_message(ob, 'left', '#332211')
        time.sleep( 0 )
        t2 = threading.Thread( target=self.playResponce, args=(ob,) )
        t2.start()


    def playResponce(self, responce) :
        x = pyttsx3.init()
        x.setProperty( 'rate', 480)
        x.setProperty( 'volume', 100 )
        x.say( responce )
        x.runAndWait()
        print( "Played Successfully......" )

    def image_press(self):
        self.show_alert_dialog()
        return Builder.load_string(KV)

    def on_bot_image_press(self):
        if not self.dialogBot :
            self.dialogBot = MDDialog(
                title="Information",
                text="AutoQA is an automated question answering AI made using NLP for answering python queries. It is based on retrival-based NLP using pythons NLTK tool-kit module. GUI is based on Kivy and KivyMD. It can answer questions regarding python language for new learners",
                buttons=[
                    MDRectangleFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_color, on_release=self.close_dialog_for_bot
                    ),
                ],
            )
        self.dialogBot.open()

    def close_dialog_for_bot(self, obj) :
        # Close alert box
        self.dialogBot.dismiss()

    def show_alert_dialog(self) :
        if not self.dialog :
            self.dialog = MDDialog(
                title="Warning",
                text="Are you want close this app?",
                buttons=[
                    MDRectangleFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Yes", text_color=self.theme_cls.primary_color, on_release=self.neat_dialog
                    ),
                ],
            )

        self.dialog.open()

        # Click Cancel Button

    def close_dialog(self, obj) :
        # Close alert box
        self.dialog.dismiss()

        # Click the Neat Button

    def neat_dialog(self, obj) :
        # Close alert box
        self.dialog.dismiss()
        # Change label text
        exit()




    def scroll_bottom(self):
        rv = self.root.ids.rv
        box = self.root.ids.box
        if rv.height < box.height:
            Animation.cancel_all(rv, 'scroll_y')
            Animation(scroll_y=0, t='out_quad', d=.5).start(rv)


if __name__ == '__main__':
    MessengerApp().run()