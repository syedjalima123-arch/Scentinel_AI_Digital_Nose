import tkinter as tk
from tkinter import ttk
import random
import threading

BG='#0b1220'; CARD='#121d2f'; TEXT='#f4f7fb'; MUTED='#9fb0c3'; BLUE='#35c7ff'; GREEN='#35d07f'; WARN='#ffb84d'; RED='#ff5d6c'
ODORS={1:('Normal Air','SAFE','No abnormal odour detected.',GREEN),2:('Smoke','DANGER','Warning! Smoke detected.',RED),3:('Gas Leak','CRITICAL','Warning! Possible gas leak detected.',RED),4:('Spoiled Food','WARNING','Spoiled-food odour pattern detected.',WARN),5:('Coffee','IDENTIFIED','Coffee-like odour pattern detected.',BLUE),6:('Flower','IDENTIFIED','Flower-like odour pattern detected.',GREEN)}

class Scentinel:
    def __init__(self,root):
        self.root=root; root.title('SCENTINEL AI - Digital Nose'); root.geometry('1100x700'); root.configure(bg=BG)
        self.c=tk.Frame(root,bg=BG); self.c.pack(fill='both',expand=True); self.title_page()
    def clear(self):
        for w in self.c.winfo_children(): w.destroy()
    def btn(self,p,text,cmd,bg=BLUE,w=22):
        return tk.Button(p,text=text,command=cmd,font=('Segoe UI',12,'bold'),width=w,bg=bg,fg='#06101b',relief='flat',cursor='hand2',padx=8,pady=9)
    def title_page(self):
        self.clear(); tk.Label(self.c,text='SCENTINEL AI',font=('Segoe UI',44,'bold'),bg=BG,fg=BLUE).pack(pady=(90,5))
        tk.Label(self.c,text='DIGITAL NOSE',font=('Segoe UI',25,'bold'),bg=BG,fg=TEXT).pack()
        tk.Label(self.c,text='Assistive odour-detection and alert simulation',font=('Segoe UI',14),bg=BG,fg=MUTED).pack(pady=10)
        tk.Label(self.c,text='AIR  →  SENSOR ARRAY  →  ESP32  →  CLASSIFIER  →  ALERT',font=('Consolas',14,'bold'),bg=BG,fg=TEXT).pack(pady=35)
        self.btn(self.c,'START SCENTINEL',self.init_page,w=25).pack()
    def init_page(self):
        self.clear(); tk.Label(self.c,text='SCENTINEL INITIALIZATION',font=('Segoe UI',28,'bold'),bg=BG,fg=TEXT).pack(pady=(25,4))
        tk.Label(self.c,text='Initializing the digital-nose software pipeline',font=('Segoe UI',12),bg=BG,fg=MUTED).pack(pady=(0,18))
        box=tk.Frame(self.c,bg=CARD,padx=35,pady=25); box.pack(padx=100,pady=20,fill='x')
        self.init_status=tk.Label(box,text='Starting system...',font=('Segoe UI',15,'bold'),bg=CARD,fg=TEXT); self.init_status.pack(pady=(0,18))
        self.progress=ttk.Progressbar(box,orient='horizontal',length=700,mode='determinate'); self.progress.pack(pady=10)
        names=['ESP32 controller','MQ-2 gas/smoke channel','MQ-135 air-quality channel','BME680 VOC/environment channel','Temperature & humidity','Audio/alert subsystem','Odour classification engine']
        self.labels=[]
        for n in names:
            x=tk.Label(box,text=f'○  {n}   [WAITING]',font=('Segoe UI',12),anchor='w',bg=CARD,fg=MUTED); x.pack(fill='x',pady=3); self.labels.append(x)
        self.i=0; self.init_step()
    def init_step(self):
        if self.i<len(self.labels):
            n=self.labels[self.i]['text'][3:].split('   [')[0]
            self.labels[self.i].config(text=f'✓  {n}   [READY]',fg=GREEN); self.progress['value']=(self.i+1)*100/len(self.labels); self.init_status.config(text=f'Initializing subsystem {self.i+1}/{len(self.labels)}...'); self.i+=1; self.root.after(450,self.init_step)
        else:
            self.init_status.config(text='SYSTEM READY — all simulated subsystems initialized',fg=GREEN); self.root.after(800,self.dashboard)
    def dashboard(self):
        self.clear(); tk.Label(self.c,text='SELECT ODOUR SCENARIO',font=('Segoe UI',28,'bold'),bg=BG,fg=TEXT).pack(pady=(25,4)); tk.Label(self.c,text='Click a numbered box to move to the detection page',font=('Segoe UI',12),bg=BG,fg=MUTED).pack(pady=(0,18))
        g=tk.Frame(self.c,bg=BG); g.pack(pady=5)
        for i,(num,name,color) in enumerate([(1,'NORMAL AIR',GREEN),(2,'SMOKE',RED),(3,'GAS LEAK',RED),(4,'SPOILED FOOD',WARN),(5,'COFFEE',BLUE),(6,'FLOWER',GREEN)]):
            r,col=divmod(i,3); tk.Button(g,text=f'{num}\n{name}',command=lambda n=num:self.detect(n),font=('Segoe UI',17,'bold'),width=18,height=4,bg=CARD,fg=color,activebackground='#1d2d45',relief='solid',bd=1,cursor='hand2').grid(row=r,column=col,padx=12,pady=12)
        tk.Label(self.c,text='Simulation values are representative placeholders for future live ESP32 sensor readings.',font=('Segoe UI',10),bg=BG,fg=MUTED).pack(pady=15)
        self.btn(self.c,'VIEW SYSTEM ARCHITECTURE',self.architecture,w=25).pack()
    def readings(self,n):
        ranges={1:(80,150,100,180,50,120,24,28,40,60),2:(700,950,500,800,400,700,30,40,30,50),3:(600,900,500,850,350,650,25,35,35,55),4:(250,450,500,750,450,800,25,32,55,80),5:(150,300,250,450,250,500,24,30,40,65),6:(100,220,200,400,180,350,23,29,45,70)}
        a=ranges[n]; return {'MQ-2':random.randint(a[0],a[1]),'MQ-135':random.randint(a[2],a[3]),'BME680 VOC':random.randint(a[4],a[5]),'Temperature':f'{random.randint(a[6],a[7])} °C','Humidity':f'{random.randint(a[8],a[9])} %'}
    def detect(self,n):
        name,status,msg,color=ODORS[n]; self.clear(); tk.Label(self.c,text='SCENTINEL ANALYSIS',font=('Segoe UI',28,'bold'),bg=BG,fg=TEXT).pack(pady=(22,4)); tk.Label(self.c,text='Sensor pattern → classification → alert',font=('Segoe UI',12),bg=BG,fg=MUTED).pack(pady=(0,15))
        main=tk.Frame(self.c,bg=BG); main.pack(fill='both',expand=True,padx=45)
        left=tk.Frame(main,bg=CARD,padx=25,pady=20); left.pack(side='left',fill='both',expand=True,padx=(0,10)); right=tk.Frame(main,bg=CARD,padx=25,pady=20); right.pack(side='right',fill='both',expand=True,padx=(10,0))
        tk.Label(left,text='DIGITAL NOSE',font=('Segoe UI',20,'bold'),bg=CARD,fg=BLUE).pack(pady=5); self.air=tk.Label(left,text='AIR  →  →  →  ◉',font=('Consolas',22,'bold'),bg=CARD,fg=TEXT); self.air.pack(pady=25)
        tk.Label(left,text='SIMULATED SENSOR READINGS',font=('Segoe UI',13,'bold'),bg=CARD,fg=MUTED).pack()
        for k,v in self.readings(n).items(): tk.Label(left,text=f'{k:<20} {v}',font=('Consolas',12),anchor='w',bg=CARD,fg=TEXT).pack(fill='x',pady=4)
        tk.Label(right,text='SCENT DETECTED',font=('Segoe UI',18,'bold'),bg=CARD,fg=MUTED).pack(pady=5); tk.Label(right,text=name.upper(),font=('Segoe UI',30,'bold'),bg=CARD,fg=color).pack(pady=8); tk.Label(right,text=f'STATUS: {status}',font=('Segoe UI',17,'bold'),bg=CARD,fg=color).pack(pady=8)
        conf=random.randint(88,97); tk.Label(right,text=f'SIMULATED CONFIDENCE: {conf}%',font=('Segoe UI',11,'bold'),bg=CARD,fg=TEXT).pack(pady=8); tk.Label(right,text=msg,font=('Segoe UI',14),bg=CARD,fg=TEXT,wraplength=380,justify='center').pack(pady=15)
        self.voice=tk.Label(right,text='🔊 VOICE ALERT READY',font=('Segoe UI',13,'bold'),bg=CARD,fg=BLUE); self.voice.pack(pady=5)
        self.btn(right,'SIMULATE VOICE ALERT',lambda:self.speak(msg),w=22).pack(pady=5); self.btn(right,'BACK TO SCENARIOS',self.dashboard,bg=GREEN,w=22).pack(pady=5); self.animate()
    def animate(self,i=0):
        self.air.config(text=['AIR   →   →   →   ◉','AIR    →   →   →   ◉','AIR     →   →   →   ◉'][i%3]); self.root.after(300,lambda:self.animate(i+1))
    def speak(self,msg):
        self.voice.config(text='🔊 SPEAKING: '+msg,fg=GREEN)
        try:
            import pyttsx3
            threading.Thread(target=lambda:(lambda e:(e.say(msg),e.runAndWait()))(pyttsx3.init()),daemon=True).start()
        except ImportError:
            self.voice.config(text='🔊 VOICE SIMULATION: '+msg+'\nInstall pyttsx3 for actual laptop speech.',fg=WARN)
    def architecture(self):
        self.clear(); tk.Label(self.c,text='SCENTINEL HARDWARE ARCHITECTURE',font=('Segoe UI',27,'bold'),bg=BG,fg=TEXT).pack(pady=(20,4)); tk.Label(self.c,text='ESP32-based digital nose — Arduino Uno is NOT used',font=('Segoe UI',12),bg=BG,fg=MUTED).pack(pady=(0,15))
        for i,(t,col) in enumerate([('AIR INLET / SAMPLE CHAMBER',BLUE),('SENSOR ARRAY\nMQ-2 + MQ-135 + BME680',GREEN),('ESP32\nDATA ACQUISITION + PROCESSING',BLUE),('ML CLASSIFIER\nPATTERN RECOGNITION',WARN),('ALERT OUTPUT\nVOICE / SPEAKER + MOBILE',GREEN)]):
            tk.Label(self.c,text=t,font=('Segoe UI',14,'bold'),bg=CARD,fg=col,padx=20,pady=12,width=45,relief='solid',bd=1).pack(pady=4)
            if i<4: tk.Label(self.c,text='↓',font=('Segoe UI',18,'bold'),bg=BG,fg=MUTED).pack()
        self.btn(self.c,'BACK TO SCENARIOS',self.dashboard,bg=GREEN,w=22).pack(pady=15)

if __name__=='__main__':
    root=tk.Tk(); Scentinel(root); root.mainloop()
