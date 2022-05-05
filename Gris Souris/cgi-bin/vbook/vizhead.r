$page .= <<EOH;  #DO NOT edit these or the last two lines.

<!------Keep variables names as is, do not change!------>
<center><table border="0" cellpadding="2" cellspacing="0" width="590" $tb_tbleclr>
  <tr>
    <td valign="middle" rowspan="3" align="center" width="110">
	<table border="0" cellpadding="0" cellspacing="0"">
	<td valign="middle" align="center">
		<a href="$vizbkScrpt?adviz=y"><img src="$pics_dir/admn3.gif" align="middle" width="110" height="110" border="0" 
		alt="Add to $siteis - a free list book - guests - visitors"></a>
      </td></tr></table>
    <td valign="middle" colspan="1" align="center" width="480">
    <b>Return to <a href="$return_url">the Main Page</a>&nbsp;&nbsp; Old&nbsp; <a href="http://www.galanter.net/guests/showguest.asp?Account=14">Guestbook</a></b></td>
  </tr><tr>
    <td valign="middle" align="center" width="480" $tb_cellclr>
    <font color="$misc_clr"><font size="$sze_3" face="$pref_fnt"><strong>
    Please feel free to <big><a href="$vizbkScrpt?adviz=y"><b>Add</b></a></big> to</font><br>
    <font size="6">$listis</strong></font></font></td>
  </tr><tr>
    <td valign="middle" colspan="1" align="center" width="480"><font size="$sze_3" face="$pref_fnt">
    If your new entry does not appear, please refresh the page.
    </font></td>
  </tr></table></center>

EOH
1;	# this line MUST remain in all 'require' files.
