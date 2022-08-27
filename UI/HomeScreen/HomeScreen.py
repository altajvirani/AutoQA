import time
from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
import pyttsx3
import threading
from BotAPI.bot import chat
from TextToSpeechAPI.TextToSpeech import playResponce

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
            source: "assets/images/box1.png"
            pos_hint: {"x": 0, "top": 1}
            padding: [0,15]
        FitImage: 
            size_hint_y: None
            allow_stretch: True
            width: dp(120)
            height: dp(120)
            source: "assets/images/box2.png"
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
                    icon: "assets/images/back.png"
                    on_press: app.on_exit_image_press()
                MDIconButton:
                    icon: "assets/images/botdp.png"
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
                        font_name: 'assets/fonts/helvetica/roundedbold.otf'
                        halign: "left"
                        valign: "bottom"
                        padding: [4,0]
                    MDLabel:
                        title: "Online"
                        text: "online"
                        font_size: '12sp'
                        font_name: 'assets/fonts/helvetica/regular.ttf'
                        halign: "left"
                        valign: "top"
                        padding: [4, 0]
                MDIconButton:
                    id: menu
                    icon: "assets/images/menu.png" 
                    on_press: app.on_menu_image_press()                 
    BoxLayout: 
        orientation: 'vertical'
        size_hint_y: 8.8
        padding: [8,0]
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
            icon: 'assets/images/send.png'
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
                radius: dp(8), dp(8), dp(8), dp(8)
                pos: self.pos
        canvas.after:
            Color:
            Line:
                rounded_rectangle: self.pos + self.texture_size + [dp(5)]
                width: 1.01
'''
Window.size = (392,700)

class AutoQA_AI( MDApp ) :
    messages = ListProperty()
    ExitDialog = None
    BotDialog = None
    MenuDialog = None

    def build(self) : #This method define in MDApp class which is baseclass of our class(AutoQA_AI)  this is used to build our app
        self.title = 'Natural Language Processing' #it is use to set title of Kivy App
        return Builder.load_string(KV)  #it loads the kv variable as string then show the ui of app using KV variable


    def send_message(self, textinput): #when user click on send button then App stop taking inputs from InputBox and storing inputs in textinput variable as well as this method is also called
        text = textinput.text #convert the input in text form
        textinput.text = '' #remove all the values from textinput variable
        if len(text) != 0: #if user enter somethings in InputBox then this condtion is excute
            self.add_user_message(text, 'right', '#2E58E0') #call the add_user_message()
            self.focus_textinput(textinput) #call the focus_textinput()
            ob = chat(text) #when everthings is fine then chat() method is call, which is method of Bot class. All the NLP logic apply in Bot Class. op varibale use to store the response given by chat() method.
            Clock.schedule_once(lambda *args : self.answer(ob), 1) #after getting response it will send answer(ob) method
            self.scroll_bottom() #this method use for scrolling

        else: # when user press send button without entering any message/request/que then is condition is execute
            message = 'Please enter Your Question!'
            toast( 'Please enter Your Question!' )
            time.sleep( 0 )
            t2 = threading.Thread( target=playResponce, args=(message,) ) #this called the playResponce api.
            t2.start()

    @staticmethod
    def focus_textinput(textinput):
        textinput.focus = True

    def add_user_message(self, text, side,
                         color) :  # This method used to add User Que/request/Message in Message List Variable in right side with Len,Text,side(right) and color. These All the value come from send_message() method.
        # create a message for the recycleview
        self.messages.append( {
            'message_id' : len( self.messages ),
            'text' : text,
            'side' : side,
            'bg_color' : color,
            'text_size' : [None, None],
        } )

    def answer(self, ob, *args): #use to display bot respon
        self.add_bot_message( ob, 'left', '#009E9E' ) #calling add_bot_message() method
        time.sleep( 0 )
        t2 = threading.Thread( target=playResponce, args=(ob,))#this called the playResponce api.
        t2.start()

    def add_bot_message(self, text, side, color): # This method used to add Bot Ans/Response/Message in Message List Variable in left side with Len,Text,side(left) and color. These All the value come from answer() method.
        # create a message for the recycleview
        self.messages.append( {
            'message_id' : len( self.messages ),
            'text' : text,
            'side' : side,
            'bg_color' : color,
            'text_size' : [None, None],
        } )

    def update_message_size(self, message_id, texture_size, max_width): #when new messages added in messages variable or when size of screen is chnage then this method call

        # when the label is updated, we want to make sure the displayed size is
        # proper
        if max_width == 0 :
            return

        one_line = dp( 50 )  # a bit of  hack, YMMV

        # if the texture is too big, limit its size
        if texture_size[0] >= max_width * 2 / 3 :
            self.messages[message_id] = {
                **self.messages[message_id],
                'text_size' : (max_width * 2 / 3, None),
            }

        # if it was limited, but is now too small to be limited, raise the limit
        elif texture_size[0] < max_width * 2 / 3 and \
                texture_size[1] > one_line :
            self.messages[message_id] = {
                **self.messages[message_id],
                'text_size' : (max_width * 2 / 3, None),
                '_size' : texture_size,
            }

        # just set the size
        else :
            self.messages[message_id] = {
                **self.messages[message_id],
                '_size' : texture_size,
            }

    def scroll_bottom(self): #this is used for scrolling
        rv = self.root.ids.rv
        box = self.root.ids.box
        if rv.height < box.height :
            Animation.cancel_all( rv, 'scroll_y' )
            Animation( scroll_y=0, t='out_quad', d=.5 ).start(rv)

   #creating Dialogboxes as per requirements

    def on_bot_image_press(self): #this method used to create bot dialog box which shows the information realted this BOT
        if not self.BotDialog :
            self.BotDialog = MDDialog(
                title="Information",
                text="AutoQA is an automated question answering AI made using NLP for answering python queries. It is based on retrival-based NLP using pythons NLTK tool-kit module. GUI is based on Kivy and KivyMD. It can answer questions regarding python language for new learners",
                buttons=[
                    MDRectangleFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_color, on_release=self.close_dialog_for_bot
                    ),
                ],
            )
        self.BotDialog.open() #use to open bot dialogbox

    def close_dialog_for_bot(self, obj): #used to close the bot dialogbox
        self.BotDialog.dismiss()

    def on_exit_image_press(self): #this method used to create exit dialog box which shows the Warning
        if not self.ExitDialog :
            self.ExitDialog = MDDialog(
                title="Warning",
                text="Are you want close this app?",
                buttons=[
                    MDRectangleFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.cloase_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Yes", text_color=self.theme_cls.primary_color, on_release=self.close_app
                    ),
                ],
            )

        self.ExitDialog.open() #open exit dialogbox

    def close_app(self, obj): #for closing app
        self.ExitDialog.dismiss()
        exit()

    def cloase_dialog(self, obj): # for closing exit dialog box
        self.ExitDialog.dismiss()

    def on_menu_image_press(self): # used to open menu dialog
        if not self.MenuDialog :
            self.MenuDialog = MDDialog(
                title="Developers",
                text=" 19. Altaj Virani \n 20. Rakesh Yadav \n 77. Manish Nayak \n 78. Yash Patil",
                buttons=[
                    MDRectangleFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_color, on_release=self.clase_menu_dialog
                    ),
                ],
            )
        self.MenuDialog.open() #open menu dialog

    def clase_menu_dialog(self, obj): #cloase menu dialog
        self.MenuDialog.dismiss()


if __name__ == '__main__' :
    AutoQA_AI().run() #used to run the app