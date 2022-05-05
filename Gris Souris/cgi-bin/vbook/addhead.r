print <<EOADD;
  <center>
<table CELLSPACING="0" CELLPADDING="2" BORDER="0" width="575">
<!---------------Add-Visitor Page HEADER---------------->
    <tr>
      <td align="center" width="100%" bgcolor="#336699"><font color="#ffffff"
      size="5"><strong>Add to $listis</strong></font></td>
    </tr><tr>
      <td align="center" width="100%" bgcolor="#ffffff"><font face="arial,helvetica"
      size="2">Please fill in the boxes below to add to $listis.<br>
      The <b><font color="#CC0000">Required</font></b><strong>*</strong> entries are: <b>Name</b>,
      <b>E-Mail</b> and <b>Comments</b>. <em>Thank you!</em></font></td>
    </tr>
<!------------------------------------------------------>
EOADD
if ($shw_icq && $list_email) {
print "     <tr><td align=\"center\" width=\"100%\"><font face=\"arial,helvetica\" size=\"2\">If you\n";
print "      have an <font color=\"#FF0000\">ICQ number</font>, you can include it too.</font></td></tr>\n";
}
print "  </table></center>\n";

1;	# this line MUST remain in all 'require' files.
