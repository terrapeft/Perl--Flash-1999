#! /usr/bin/perl

open (IN, "0frlinks.dat");
($i_name, $i_link)=split(/\|/, <IN>);
($y_name, $y_link)=split(/\|/, <IN>);
($d_name, $d_link)=split(/\|/, <IN>);
($r_name, $r_link)=split(/\|/, <IN>);

&getmidi;
foreach $s1 (@files2) {
  $lst .= "     <option value=\"$s1\">$s1</option>\n"};



print <<"cooper";
Content-Type: text/html


<html>

<head>
<meta http-equiv="Content-Language" content="ru">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="GENERATOR" content="Microsoft FrontPage 4.0">
<meta name="ProgId" content="FrontPage.Editor.Document">
<title>Центр управления полетом</title>
<STYLE TYPE="text/css">
A:hover {
   color: #FF3300;
   text-decoration: none;
}
</STYLE>

</head>

<body style="font-family: Arial; font-size: 10pt" bgcolor="#808080" link="#FFFF00" vlink="#FFFF00">
<table border="0" width="100%" cellspacing="0" cellpadding="0">
  <tr>
    <td width="100%" bgcolor="#00FF00" height="3"></td>
  </tr>
  <tr>
    <td width="100%" height="3"></td>
  </tr>
  <tr>
    <td width="100%" bgcolor="#00FF00" height="2"></td>
  </tr>
  <tr>
    <td width="100%" height="3"></td>
  </tr>
  <tr>
    <td width="100%" bgcolor="#00FF00" height="1"></td>
  </tr>
  <tr>
    <td width="100%" height="3">
      <p align="center"></td>
  </tr>
  <tr>
    <td valign="middle" nowrap>
      <p align="center"><font size="5">&nbsp;<b><i><font color="#FFFF00">&nbsp;</font><font color="#00FF00">G</font><font color="#FF0000">r</font><font color="#0000FF">i</font><font color="#FFFF00">s</font><font color="#00FF00">
      </font><font color="#00FFFF">S</font><font color="#FFFFFF">o</font><font color="#FF00FF">u</font><font color="#000080">r</font><font color="#FF0000">i</font><font color="#FFFF00">s</font><font color="#00FF00">' Центр
      Управления</font></i></b></font></p>
    </td>
  </tr>
  <tr>
    <td width="100%" height="3">
      <p align="right"><font size="1">.</font></td>
  </tr>
  <tr>
    <td width="100%" bgcolor="#00FF00" height="1"></td>
  </tr>
</table>
<br>
<table border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td width="100%" bgcolor="#C0C0C0"><span style="background-color: #00FF00">Смена
        фоновой музыки на титульной странице</span>
    </td>
  </tr>
  <tr>
    <td width="100%" bgcolor="#C0C0C0">
      <p><span style="background-color: #FFFF00"><font size="2">1 этап -
      закачка необходимого файла на сайт</font></span></p>
        <ul>
          <li><font size="2">Нажми кнопку ОБЗОР, выбери
            нужный файл</font></li>
          <li><font size="2">Нажми кнопку <span style="background-color: #FF0000">Закачать</span></font></li>
        </ul>

        <FORM ENCTYPE="multipart/form-data" ACTION="upload.pl" METHOD="POST">
        <TABLE BORDER=0 WIDTH="460">
        <TR><TD ALIGN=RIGHT>Файл 1:</TD><TD>
            <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </TD>        </TR>        <TR>
            <TD ALIGN=RIGHT>      Файл 2:
            </TD> <TD> <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </TD> </TR>  <TR>
            <TD ALIGN=RIGHT>           Файл 3:
            </TD> <TD> <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </TD> </TR> <TR>  <TD ALIGN=RIGHT>  Файл 4:  </TD>
            <TD>  <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </TD>     </TR>	<TR><TD COLSPAN=2>&nbsp;<BR></TD>
		</TR>      <TR>        <TD>
                <INPUT TYPE="SUBMIT" VALUE="Закачать!" style="font-family: Arial; color: #000000; background-color: #FF0000">
            </TD>        <TD ALIGN=RIGHT>
                <INPUT TYPE="RESET" VALUE="Сбросить" style="font-family: Arial; color: #000000; background-color: #0000FF">
            </TD>     </TR>    </TABLE>     </FORM>

    </td>
  </tr>
  <tr>
    <td width="100%" bgcolor="#C0C0C0">

<span style="background-color: #FFFF00"><font size="2">2 этап - выбор
и установка требуемого файла</font></span>
        <ul>
          <li><font size="2">Выбери файл в выпадающем меню
            - если там нет закачанного файла -
            нажми обновление страницы</font></li>
          <li><font size="2">Нажми кнопку <span style="background-color: #FF0000">Сделать</span></font></li>
        </ul>

<form method="POST" action="amidi.cgi">
  Выбор MIDI файла&nbsp;&nbsp; <select size="1" name="mzmid">$lst
  </select><input type="submit" value="Сделать" name="B1" style="font-family: Arial; color: #000000; background-color: #FF0000">
</form>
    </td>
  </tr>
</table>
<br>
<p>
<br>

<form method="POST" action="alink.cgi">
  <table border="0" cellspacing="1" bgcolor="#FFFFFF" width="100%">
    <tr>
      <td width="60%" bgcolor="#C0C0C0" colspan="2"><span style="background-color: #00FF00">Изменение
        гиперссылок</span> </td>
    </tr>
    <tr>
      <td width="10%" bgcolor="#C0C0C0"><b><font size="3">$i_name</font></b> </td>
      <td width="50%" bgcolor="#C0C0C0"><input type="text" name="T1" size="100" value="$i_link" style="border-style: dotted; border-color: #000000"></td>
    </tr>
    <tr>
      <td width="10%" bgcolor="#C0C0C0"><b><font size="3">$d_name</font></b> </td>
      <td width="50%" bgcolor="#C0C0C0"><input type="text" name="T2" size="100" value="$d_link" style="border-style: dotted; border-color: #000000"></td>
    </tr>
    <tr>
      <td width="10%" bgcolor="#C0C0C0"><b><font size="3">$y_name</font></b> </td>
      <td width="50%" bgcolor="#C0C0C0"><input type="text" name="T3" size="100" value="$y_link" style="border-style: dotted; border-color: #000000"></td>
    </tr>
    <tr>
      <td width="10%" bgcolor="#C0C0C0"><b><font size="3">$r_name</font></b> </td>
      <td width="50%" bgcolor="#C0C0C0"><input type="text" name="T4" size="100" value="$r_link" style="border-style: dotted; border-color: #000000"></td>
    </tr>
    <tr>
      <td width="100%" colspan="2" bgcolor="#C0C0C0">
        <p align="left"><input type="submit" value="Сделать" name="B1" style="font-family: Arial; color: #000000; background-color: #FF0000"><input type="reset" value="Сбросить" name="B2" style="font-family: Arial; color: #000000; background-color: #0000FF"></td>
    </tr>
  </table>
</form>
<br>
<div align="center">
  <center>
  <table border="0" cellspacing="0" cellpadding="0" bgcolor="#000000">
    <tr>
      <td width="100%">
        <p align="center"><a href="../webmster.html" style="text-decoration: none"><b>LG Daily Stats</b></a><span style="background-color: #000000"><font face="Arial Black" size="2" color="#FFFFFF">|</font><font color="#FFFFFF">&nbsp;</font><font face="Arial Black" size="2" color="#FFFFFF"><a href="../april/index.htm" STYLE="text-decoration: none">Апрель
        </a>| <a href="../main/index.htm"><span style="text-decoration: none">Я самая</span></a>
| <a href="../gallery/index.htm"><span style="text-decoration: none">Галерея</span></a>
| <a href="../friends/index.htm"><span style="text-decoration: none">Друзья</span></a>
| <a href="http://gris-souris.virtualave.net/vizbook/vizbook.htm" STYLE="text-decoration: none"><span style="text-decoration: none">Гостевая</span></a>
        | <a href="../links/main.htm" target="main"><span style="text-decoration: none">Линки</span></a>
| <a href="../utility/index.htm"> <span style="text-decoration: none; background-color: #000000">Утилиты</span></a></font></span></td>
    </tr>
  </table>
  </center>
</div>
</body>
</html>

cooper

sub getmidi {
opendir(DIR,"../midi") || die ('Error Accessing MIDI Directory'); 
@files = sort(readdir(DIR));
closedir(DIR);
for($s1 = @files; $s1 >= 0; $s1--) {
	if ($files[$s1] !~ /^\d+(.mid|.wav)/i) {
		push(@files2,$files[$s1]) if $files[$s1] =~ /(.mid|.wav)/i;
		splice(@files,$s1,1);
	}
}
@files2 = sort(@files2);
}

