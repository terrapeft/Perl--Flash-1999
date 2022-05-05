#! /usr/bin/perl

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
<STYLE TYPE="text/css">
A:hover {
   color: #FF3300;
   text-decoration: none;
}
</STYLE>

</head>

<body style="font-family: Arial; font-size: 10pt" bgcolor="#808080" link="#FFFF00" vlink="#FFFF00">

<table border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td width="100%" bgcolor="#C0C0C0"><span style="background-color: #00FF00">Смена
        фоновой музыки на титульной странице</span>
    </td>
  </tr>
  <tr>

        <FORM ENCTYPE="multipart/form-data" ACTION="upload.pl" METHOD="POST">
        <TABLE BORDER=0 WIDTH="460">
        <TR><TD ALIGN=RIGHT>File 1:</TD><TD>
            <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </TD>        </TR>        <TR>
            <TD ALIGN=RIGHT>      File 2:
            </TD> <TD> <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </TD> </TR>  <TR>
            <TD ALIGN=RIGHT>           File 3:
            </TD> <TD> <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </TD> </TR> <TR>  <TD ALIGN=RIGHT>  File 4:  </TD>
            <TD>  <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </TD>     </TR>	<TR><TD COLSPAN=2>&nbsp;<BR></TD>
		</TR>      <TR>        <TD>
                <INPUT TYPE="SUBMIT" VALUE="Upload File(s)!">
            </TD>        <TD ALIGN=RIGHT>
                <INPUT TYPE="RESET" VALUE="Reset Form">
            </TD>     </TR>    </TABLE>     </FORM>

  </tr>
  <tr>
    <td width="100%" bgcolor="#C0C0C0">

<form method="POST" action="amidi.cgi">
  Выбор MIDI файла&nbsp;&nbsp; <select size="1" name="mzmid">$lst
  </select><input type="submit" value="Сделать" name="B1" style="font-family: Arial; font-size: 8pt; color: #000000; background-color: #FF0000">
</form>
    </td>
  </tr>
</table>
<br>
<p>
<br>

</body>
</html>

cooper

sub getmidi {
opendir(DIR,"../midi") || &showErr('Error Accessing Pics Directory'); 
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

