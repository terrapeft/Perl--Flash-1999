       // ___________________________________________________________ //
       // ----------------------------------------------------------- //
       //                        Information                          //
       // Copyright (C) 2000 Killer John  e-mail: killerjohn@mail.ru  //
       //             http://right-now.virtualave.net/                //
       //   Original version distributed free without any warranty.   //
       //      This copyright couldn't be modified in any way.        //
       // Also decoder for decoding russian text into Finetype format //
       //     supplied. There is no need to decode english text.      //
       //              Just send me e-mail for decoder.               //
       // ___________________________________________________________ //
       // ----------------------------------------------------------- //


var directory
    extension = ".gif"   //___ ����७�� � "�������"

//___ ���� � �㪢�� �⭮�⥫쭮 ��뢠�饩 ��࠭���  

function imageseek (dir)
{
directory=dir
}

//___ ��⠢��� ������ ��ப�

function breakit()
{
document.write("<br>")
}

//___ �⠢�� ���� (link) �� 㪠������ ���⨭�� (filename)

function linker(filename,link)
{
document.write("<p align=\"center\">")
document.write("<a href=\""+link+"\"><img border=\"0\" src=\"" + filename + "\"></a>") 
document.write("</p>")
}

//___ ��ࠢ������� (tab) - "center",  "right", "left".
//___ ������砥� ��砫� ��� ����� �뢮������ ⥪��
//___ 0 - ��砫�, 1 - �����.

function alingment (tab,end)
{
if (end==0) {document.write("<p align=\""+tab+"\">")}
else {document.write("</p>")}
}

//___ ����⢥��� ���.
//___ line - ᠬ ⥪��, 
//___
//___ interval - �᫨ 0 - ��� ���ࢠ�� ����� ��ப��� 1 - ����, 
//___ 2 - ᯫ�譮� ��⮪ (��� ࠧ������� �� ��ப�)
//___
//___ widthq, heghtq - �ਭ� � ���� ��㭪�, �᫨ 0 - � ������ 
//___ �����騩 ࠧ���
//___
//___ lang - �᫨ "rus", � �� �㤥� "��ॢ�������" �� ���᪨�, 
//___ �᫨ �� ���� ��㣮� - �㤥� "��������" ��� ����

function finetype(line, interval, widthq, heightq, lang)

{
for (var i=0; i<line.length; i++)
{

letter=line.charAt(i);

if (lang=="rus") {
if (letter=="~") 
{letter+= line.charAt(i+1) + line.charAt(i+2); i+=2 }; 

if (letter=="a") {letter="az"}; 
if (letter=="b") {letter="buki"}; 
if (letter=="v") {letter="vedi"}; 
if (letter=="g") {letter="glagol"}; 
if (letter=="d") {letter="dobro"}; 
if (letter=="e") {letter="est"}; 
if (letter=="j") {letter="jivete"}; 
if (letter=="z") {letter="zemla"}; 
if (letter=="i") {letter="ije"}; 
if (letter=="~yi") {letter="yi"}; 
if (letter=="k") {letter="kako"}; 
if (letter=="l") {letter="ludi"}; 
if (letter=="m") {letter="mislete"}; 
if (letter=="n") {letter="nash"}; 
if (letter=="o") {letter="on"}; 
if (letter=="p") {letter="pokoy"}; 
if (letter=="r") {letter="rtsi"}; 
if (letter=="s") {letter="slovo"}; 
if (letter=="t") {letter="tverdo"}; 
if (letter=="u") {letter="ipsilon"}; 
if (letter=="f") {letter="fert"}; 
if (letter=="h") {letter="her"}; 
if (letter=="~ts") {letter="tsi"}; 
if (letter=="~ch") {letter="cherv"}; 
if (letter=="~sh") {letter="sha"}; 
if (letter=="~sc") {letter="scha"}; 
if (letter=="~er") {letter="er"}; 
if (letter=="~ei") {letter="eri"}; 
if (letter=="~ey") {letter="ery"}; 
if (letter=="~ob") {letter="oborotnoe"}; 
if (letter=="~yu") {letter="yu"}; 
if (letter=="~ys") {letter="yus"}; 
}

if (letter==" ") {letter="sp"}; 
if (letter==":") {letter="dv"}; 
if (letter=="?") {letter="que"}; 
if (letter=="\"") {letter="quo"}; 
if (letter=="\'") {letter="oqu"}; 
if (letter=="\\") {letter="slash_"}; 
if (letter=="/") {letter="slash"}; 
if (letter=="#") {letter="tur"}; 
if (letter=="~~~") {letter="kryak"}; 
 
if (widthq==0)
{ tell=directory+letter+extension;
  document.write("<img src=\"" + tell + "\">") } else

{ tell=directory+letter+extension;
document.write("<img src=\"" + tell + "\""+ " width=\""+widthq+ "\"" + " height=\"" + heightq+"\"" +">") 
}

}
if (interval==0) {document.write("<br>")} 
if (interval==1) {document.write("<br><br>")} 
if (interval==2) {document.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")} 

}

