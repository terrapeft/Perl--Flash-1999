unit _decoder;

interface

uses
  Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs,
  Buttons, StdCtrls, ComCtrls, ExtCtrls, Menus;

type
  TForm1 = class(TForm)
    GroupBox1: TGroupBox;
    eng: TRadioButton;
    GroupBox2: TGroupBox;
    left: TRadioButton;
    center: TRadioButton;
    right: TRadioButton;
    GroupBox3: TGroupBox;
    files: TRadioButton;
    window: TRadioButton;
    Open: TOpenDialog;
    GroupBox4: TGroupBox;
    dva: TRadioButton;
    odin: TRadioButton;
    GroupBox5: TGroupBox;
    SpeedButton2: TSpeedButton;
    SpeedButton1: TSpeedButton;
    Edit1: TEdit;
    GroupBox6: TGroupBox;
    CheckBox1: TCheckBox;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    rus: TRadioButton;
    wind: TRadioButton;
    Memo1: TMemo;
    GroupBox7: TGroupBox;
    StatusBar1: TStatusBar;
    noin: TRadioButton;
    yesin: TRadioButton;
    potok: TRadioButton;
    procedure SpeedButton1Click(Sender: TObject);
    procedure SpeedButton2Click(Sender: TObject);
    procedure Edit1DblClick(Sender: TObject);
    procedure CheckBox1Click(Sender: TObject);
    procedure centerMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure leftMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure rightMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure CheckBox1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox2MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure windowMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure filesMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox3MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure odinMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure dvaMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox4MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure rusMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure engMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure Memo1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox6MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure StatusBar1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure windMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure SpeedButton1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox5MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure Edit1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure noinMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure potokMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure GroupBox7MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure yesinMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.DFM}
procedure rus;
begin
end;
procedure TForm1.SpeedButton1Click(Sender: TObject);

var t,g:textfile;
    ch:char;
    st:string[3];
    filename:string;
    {en,pot:byte;}
begin
if files.Checked then begin
if open.execute then
filename:=open.filename;
assignfile(t,filename);
end else if

wind.Checked then begin
memo1.Lines.SaveToFile('in');
assignfile(t,'in');
end else
begin
assignfile(t,'in');
end;

assignfile(g,'out');
reset(t);
rewrite(g);

writeln(g,'<script type="text/javascript">');

writeln(g,'imageseek("'+edit1.text+'")');

if left.Checked then
writeln(g,'alingment("left",0)')else
if right.Checked then
writeln(g,'alingment("right",0)')else
writeln(g,'alingment("center",0)');


repeat
if dva.Checked then
write(g,'finetype("') else write(g,'finetype(''');

repeat
read(t,ch);


{if (ch in [#65..#90]) or (ch in [#97..#122])
then begin
 if eng.Checked=false then
    begin eng.Checked:=true; en:=1 end;
 if potok.Checked=false then
    begin potok.Checked:=true; pot:=1 end;
end else
begin
 if en=1 then eng.Checked:=false;
 if pot=1 then potok.Checked:=false;
end;}


case ch of
#128,#160: st:='a';
#129,#161: st:='b';
#130,#162: st:='v';
#131,#163: st:='g';
#132,#164: st:='d';
#133,#165: st:='e';
#134,#166: st:='j';
#135,#167: st:='z';
#136,#168: st:='i';
#137,#169: st:='~yi';
#138,#170: st:='k';
#139,#171: st:='l';
#140,#172: st:='m';
#141,#173: st:='n';
#142,#174: st:='o';
#143,#175: st:='p';
#144,#224: st:='r';
#145,#225: st:='s';
#146,#226: st:='t';
#147,#227: st:='u';
#148,#228: st:='f';
#149,#229: st:='h';
#150,#230: st:='~ts';
#151,#231: st:='~ch';
#152,#232: st:='~sh';
#153,#233: st:='~sc';
#154,#234: st:='~er';
#155,#235: st:='~ei';
#156,#236: st:='~ey';
#157,#237: st:='~ob';
#158,#238: st:='~yu';
#159,#239: st:='~ys';
else st:=ch end;
write(g,st);
until eoln(t);
read(t,ch);
read(t,ch);

if dva.checked then begin
 if noin.Checked then
 write(g,'","0"') else
 if yesin.Checked then
 write(g,'","1"') else
 if potok.Checked then
 write(g,'","2"')
end else
   begin
 if noin.Checked then
 write(g,''',"0"') else
 if yesin.Checked then
 write(g,''',"1"') else
 if potok.Checked then
 write(g,''',"2"')
end;

if checkbox1.Checked then begin
if ((edit2.text<>'') and (edit3.text<>'')) then
write(g,',"' + edit2.text + '","'+ edit3.text + '"') else
write(g,',"0","0"');
end else write(g,',"0","0"');

if rus.Checked then
writeln(g,',"rus");') else
if eng.Checked then
writeln(g,',"eng");');

until eof(t);

writeln(g,'alingment("",1)');
writeln(g,'</script>');
closefile(t);
closefile(g);

memo1.Lines.LoadFromFile('out');
erase(g);
memo1.SelectAll;
memo1.CopyToClipboard;

end;

procedure TForm1.SpeedButton2Click(Sender: TObject);
begin
close
end;

procedure TForm1.Edit1DblClick(Sender: TObject);
begin
edit1.text:='<SCRIPT TYPE="text/javascript" SRC="code/finetype.js"></SCRIPT>';
edit1.SelectAll;
edit1.CopyToClipboard;
end;


procedure TForm1.CheckBox1Click(Sender: TObject);
begin
if checkbox1.Checked then begin
label1.Enabled:=true;
label2.Enabled:=true;
edit2.Enabled:=true;
edit3.Enabled:=true end else
begin
label1.Enabled:=false;
label2.Enabled:=false;
edit2.Enabled:=false;
edit3.Enabled:=false end
end;

procedure TForm1.centerMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Выровнять посередине';
end;

procedure TForm1.leftMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Выровнять по левому краю';
end;

procedure TForm1.rightMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Выровнять по правому краю';

end;

procedure TForm1.CheckBox1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Размер символа (картинки, то бишь) в пикселях';
end;

procedure TForm1.GroupBox2MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.windowMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Брать исходный текст в файле "in", того же каталога что и исполняемая программа';
end;

procedure TForm1.filesMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Брать исходный текст из выбранного файла';
end;

procedure TForm1.GroupBox3MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.odinMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Если в тексте есть двойные кавычки - выбирай это';

end;

procedure TForm1.dvaMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Если в тексте есть одинарные кавычки - выбирай это';

end;

procedure TForm1.GroupBox4MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.rusMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Текст будет считаться русским';

end;

procedure TForm1.GroupBox1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.engMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Текст будет считаться английским';

end;

procedure TForm1.Memo1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.GroupBox6MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.StatusBar1MouseMove(Sender: TObject; Shift: TShiftState;
  X, Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.windMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Брать исходный текст из окошка слева - из-за проблем с кодировками может работать неверно';

end;

procedure TForm1.SpeedButton1MouseMove(Sender: TObject; Shift: TShiftState;
  X, Y: Integer);
begin
statusbar1.SimpleText:='... а также автокопирование в буфер без лишних телодвижений';

end;

procedure TForm1.GroupBox5MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.Edit1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Путь к каталогу с буквицей';

end;

procedure TForm1.noinMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Без интервала между строками (тег <br>)';

end;

procedure TForm1.potokMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='Сплошной поток, без разделения на строки';

end;

procedure TForm1.GroupBox7MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='';

end;

procedure TForm1.yesinMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
statusbar1.SimpleText:='С интервалом';

end;

end.
