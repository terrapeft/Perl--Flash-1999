sub wintokoi {
    my $pvdcoderwin=shift;
    $pvdcoderwin=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\xE1\xE2\xF7\xE7\xE4\xE5\xF6\xFA\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF2\xF3\xF4\xF5\xE6\xE8\xE3\xFE\xFB\xFD\xFF\xF9\xF8\xFC\xE0\xF1\xC1\xC2\xD7\xC7\xC4\xC5\xD6\xDA\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD2\xD3\xD4\xD5\xC6\xC8\xC3\xDE\xDB\xDD\xDF\xD9\xD8\xDC\xC0\xD1/;
return $pvdcoderwin;
}

sub do_add_head {
	require $add_heada;
}
sub add_entry {
print <<EOADD;
<form METHOD="POST" ACTION="$vizbkScrpt" align="center">
	<input TYPE="hidden" name="addfrm" value="y">
   <center>
<table CELLSPACING="0" CELLPADDING="1" BORDER="0" width="575"><tr>
<td bgcolor="#E0E0E0" align="center"><table CELLSPACING="0" CELLPADDING="2" BORDER="0" width="100%">
    </tr><tr>
      <th colspan="2" align="center" width="100%" bgcolor="#E5E5E5">$defont<a HREF="$htm_url"><b>Back to the List</b></a></FONT></th>
    </tr><tr><th ALIGN="right" nowrap bgcolor="#E5E5E5">$defont Your Name<font color="#CC0000">*</font>: </FONT></th>
      <td align="left" bgcolor="#E5E5E5"><input TYPE="text" NAME="vizname" SIZE="30" VALUE="$FORM{'vizname'}"></td>
    </tr><tr><th ALIGN="right" bgcolor="#E5E5E5">$defont E-Mail<font color="#CC0000">*</font>: </FONT></th>
      <td align="left" bgcolor="#E5E5E5"><input TYPE="text" NAME="email" SIZE="30" VALUE="$FORM{'email'}">
EOADD
if ($shw_icq) {
	print "	 $defont<b>ICQ#:</b></FONT> <input TYPE=\"text\" NAME=\"icq\" SIZE=\"15\" VALUE=\"$FORM{'icq'}\">\n";
}
	print "	 </td></tr>\n";
if ($shw_cmpny) {
	print "    <tr><th ALIGN=\"right\" bgcolor=\"#E5E5E5\">$defont Company: </FONT></th>\n";
	print "      <td align=\"left\" bgcolor=\"#E5E5E5\"><input TYPE=\"text\" NAME=\"cmpny\" SIZE=\"30\" VALUE=\"$FORM{'cmpny'}\"></td></tr>\n";
}
if ($shw_miscbox) {
	print "    <tr><th ALIGN=\"right\" bgcolor=\"#E5E5E5\">$defont $miscbox_txt: </FONT></th>\n";
	print "      <td align=\"left\" bgcolor=\"#E5E5E5\"><input TYPE=\"text\" NAME=\"miscbox\" SIZE=\"$miscbox_wid\" VALUE=\"$FORM{'miscbox'}\"></td></tr>\n";
}
if ($shw_drpdwn) {
	print "    <tr><th ALIGN=\"right\" bgcolor=\"#E5E5E5\">$defont $drpdwn_txt: </FONT></th>\n";
	print "      <td align=\"left\" bgcolor=\"#E5E5E5\"><select name=\"dlist\" size=\"1\">\n";
	$s2 = "";
	foreach $s1 (@dropdwn_items) {
		if ($FORM{dlist} && $FORM{dlist} eq $s1) {$s2 = " selected ";}
		print "      <option$s2>$s1</option>\n";
		$s2 = "";
	}	
      print "      </select>$defont <em>OR</em> <b>Other:</b></FONT> <input TYPE=\"text\" NAME=\"droptxt\" SIZE=\"$droptxt_wid\" VALUE=\"$FORM{'droptxt'}\"></td></TR>\n";
}
if ($shw_url) {
    print "      <tr><th ALIGN=\"right\" bgcolor=\"#E5E5E5\">$defont URL: </FONT></th>\n";
    print "        <td align=\"left\" bgcolor=\"#E5E5E5\"><input TYPE=\"text\" NAME=\"url\" SIZE=\"50\" VALUE=\"$FORM{'url'}\"></td>\n";
    print "      </tr>\n";
}
if ($shw_city) {
    print "        <th ALIGN=\"right\" bgcolor=\"#E5E5E5\">$defont City: </FONT></th>\n";
    print "        <th align=\"left\" bgcolor=\"#E5E5E5\"><input TYPE=\"text\" NAME=\"city\" SIZE=\"14\" VALUE=\"$FORM{'city'}\">$defont State: </FONT><input TYPE=\"text\"\n";
    print "        NAME=\"state\" SIZE=\"10\" VALUE=\"$FORM{'state'}\">$defont Country: </FONT><input TYPE=\"text\" NAME=\"cntry\" SIZE=\"15\" VALUE=\"$FORM{'cntry'}\"></th>\n";
}
print <<EOADD;
    </tr><tr>
	<th valign="top" ALIGN="right" bgcolor="#E5E5E5">$defont Comments<font color="#CC0000">*</font>&nbsp;: <font size="1"><BR>$mmax&nbsp;char&nbsp;max&nbsp;</font></FONT></th>
      <td align="left" bgcolor="#E5E5E5"><textarea NAME="msg" wrap="on" COLS="55" ROWS="6">$FORM{'msg'}</textarea></td></tr>
EOADD
if ($allow_pics) {
print <<EOADD;
    <tr><td valign="top" ALIGN="right" bgcolor="#E5E5E5">$defont<b>Picture: </b></FONT></td>
      <td align="left" bgcolor="#E5E5E5">$defont &#149; Easily <b>add your own picture</b> to this list.<br>$i_we would like 
	to include a small picture of you next to your entry. When you submit your entry you will 
	receive a confirmation e-mail containing simple instructions and a unique ID; a very easy 
	process. <em>Thank you</em></FONT></td></tr>
EOADD
}
print <<EOADD;
    <tr><td bgcolor="#E5E5E5">&nbsp;</td>
      <th bgcolor="#E5E5E5"><input TYPE="submit" VALUE="Submit Your Entry"> <input TYPE="reset"></th>
    </tr><tr>
      <td colspan="2" align="center" width="100%" bgcolor="#E5E5E5">$defont<strong><a HREF="$htm_url">Back to the List</a></strong><BR>
      <small><BR>VizBook v1.56, copyright 1999 - dtp-aus.com</small></FONT></td>
    </tr></table></td></tr></table></center>
</form></center><P>&nbsp;</body></html>
EOADD
exit;
}
sub save_entry {
	($wrds = $FORM{'msg'}) =~ s/(\s)*/ /g;
	$wrds =~ s/\W[^ ]/_/g;
	if ($wrds =~ /(\b\w{75,}\b)/) {&showErr('Comments Not Acceptable');}
	$FORM{'msg'} =~ s/\cM\n/\n/g;
	$FORM{'msg'} =~ s/(\s)+$//;
	$FORM{'msg'} =~ s/\n(\n*)/<br>/g;
	@forms = keys (%FORM);
	foreach $item (@forms)	{
     		foreach $s1 (@low_lifes) { $FORM{$item} =~ s/\b$s1\b/.../gi; }   }
if ($FORM{'addfrm'}) {
	$FORM{'email'} =~ tr/[A-Z]/[a-z]/;
	if (length($FORM{'icq'}) > 9 || $FORM{'icq'} =~ /\D+/) {&resubmit_add('ICQ# Error');}
	if ($FORM{'cmpny'} && length($FORM{'cmpny'}) > 30) {&resubmit_add('COMPANY Name too long');} 
	if ($FORM{'miscbox'} && length($FORM{'miscbox'}) > 30) {&resubmit_add("$miscbox_txt Entry too long");} 
	if ($FORM{'droptxt'} && length($FORM{'droptxt'}) > 30) {&resubmit_add("$drpdwn_txt Entry too long");} 
	if (length($FORM{'city'}) > 15) {$FORM{'city'} = substr($FORM{'city'},1,15);}
	if (length($FORM{'state'}) > 15) {$FORM{'state'} = substr($FORM{'state'},1,15);}
	if (length($FORM{'cntry'}) > 18) {$FORM{'cntry'} = substr($FORM{'cntry'},1,18);}

	($tmp = $FORM{'vizname'}) =~ s/\s//g; if ($tmp eq "") {&resubmit_add('Bad NAME Entry Detected');} 
	if (length($FORM{'url'}) > 7 && $FORM{'url'} !~ /\Ahttps?:\/\/.+\.[a-z]{2,3}($|\/)/i) {&resubmit_add('URL Error Detected');}
	if (length($FORM{'url'}) < 13) {$FORM{'url'} = "";}  
	if (length($FORM{'vizname'}) > 30) {$FORM{'vizname'} = substr($FORM{'vizname'},1,30); &resubmit_add('NAME too long');}
	if (!&chk_addr($FORM{'email'})) {&resubmit_add('Bad Email Address Detected');}
	($tmp = $FORM{'msg'}) =~ s/\s//g; if ($tmp eq "") {&resubmit_add('COMMENTS Error Detected');}
	if (length($FORM{'msg'}) > $mmax) {$FORM{'msg'} = substr($FORM{'msg'},1,$mmax); &resubmit_add("COMMENTS too long - $mmax char max");}

		&date_time(0);
			&read_rcrds; 
	open(RF,">>$records_url") || &showErr('Records-File Update Failure');
	 eval" flock(RF,2)";
		$idnumb = 10110;
		foreach $s1 (@vizrcrds){ 
		($numb) = split(/\|/,$s1);
		$allnumbs .= "$numb ";}
			srand(time^$$);
		while ($allnumbs =~ /$idnumb/) {$idnumb = &rndnumba;}
	if ($FORM{'droptxt'}) {$FORM{'dlist'} = ""};
	$new_rcrd = "$idnumb|0|$FORM{'vizname'}|$FORM{'email'}|$FORM{'icq'}|$FORM{'cmpny'}|$FORM{'url'}|$FORM{'miscbox'}|";
	$new_rcrd .= "$FORM{'dlist'}|$FORM{'droptxt'}|$FORM{'city'}|$FORM{'state'}|$FORM{'cntry'}||$datein|$FORM{'msg'}\n";
		print RF $new_rcrd;
	 eval" flock(RF,8)";
	close(RF);

	&make_page;
		&send_mail if $thanks_mail;
			&tell_me if $wbmstr_notify;
}
exit(0);
}
sub rndnumba {
	local($s1) = "00000";
	local($s2) = (1 + int(rand(99989)));
	return (substr($s1,1,length($s1) - length($s2)).$s2);
}
sub chk_addr {
    local($chk) = $_[0];
    if ($chk =~ /(.*@.*\.[a-zA-Z]{2,3}$)/ && $chk !~ /(^\.)|(\.$)|(\|)|( )|(\.\.)|(@\.)|(\.@)|(@.*@)/) { return(1); }
    else { return(0); }
}
sub send_mail {
		require $mailmsg;
	($datetime = &date_time(&date_time(0))) =~ s/\:<small>.*<\/small>//g;
	$sendto = "$webmstr?subject=$idnumb $FORM{'vizname'}";
	$sendto =~ s/ /_/g;
	open (MAIL,"|$mailprog -t") || &showErr('Mail Program Access');
        $vich666=wintokoi($FORM{'vizname'});
	print MAIL "To: $FORM{'email'} ($vich666)\n";
	print MAIL "From: $webmstr\n";
        $vcc=wintokoi($listis);
	print MAIL "Subject: Addition to $vcc\n\n";
	print MAIL "Local Time: $datetime\n";
	print MAIL "--------------------------------------\n";
	print MAIL "$sndback";
if ($allow_pics) { 
	print MAIL "You can also send a photograph of yourself to the webmaster,\n";
	print MAIL "which $i_we would be pleased to display with your comments.\n";
	print MAIL "All you have to do is resize a .gif or .jpg bitmap image,\n";
	print MAIL "or get a friend to, and add it as an e-mail \"attachment\" to: \n";
        $vk=wintokoi($sendto);
	print MAIL "$vk \n";
	print MAIL "The image file MUST be named $idnumb.(gif/jpg), because this\n";
	print MAIL "is the unique ID# for \"$vich666\", and the picture\n";
	print MAIL "(a .jpg or .gif bitmap) size MUST BE exactly 60W X 60H pixels.\n\n";
	print MAIL "As $i_we will not alter any images, wrong sized images or\n";
	print MAIL "unsuitable non-facial portraits will be rejected!\n\n";
	print MAIL "REMEMBER to use the address and subject line displayed above\n";
	print MAIL "- or simply try to double click on it in your e-mail program.\n";
	print MAIL "Your picture should then be installed within a couple of days.\n\n";
}
	print MAIL "PS: $i_we hope you will return again soon.\n";
	print MAIL "---------------------------------------\n\n";
	print MAIL "This confirmation message was sent from:\n";
	print MAIL "$htm_url Thank you.\n\n";
	print MAIL "  IP# : $ENV{'REMOTE_ADDR'}\n";
	close (MAIL);
}
sub tell_me {
	if (($ENV{'REMOTE_ADDR'} eq $ENV{'REMOTE_HOST'} || !$ENV{'REMOTE_HOST'}) && $ENV{'REMOTE_ADDR'} =~ /(\d+)\.(\d+)\.(\d+)\.(\d+)/) {
		$pk = pack('C4', $1, $2, $3, $4);
		$cnvrt = (gethostbyaddr($pk, 2))[0];
		if ($cnvrt) {$ENV{'REMOTE_HOST'} = $cnvrt;}    }
	$FORM{'msg'} =~ s/<br>(<br>)*/\n/g;
	$FORM{'msg'} =~ s/\&amp\;/\&/g;
	$FORM{'msg'} =~ s/\&quot\;/"/g;
	$FORM{'msg'} =~ s/\&lt\;/\{/g unless $allow_tgs == 1;
	$FORM{'msg'} =~ s/\&gt\;/\}/g unless $allow_tgs == 1;
        $FORM{'msg'} =~ s/<.*?>//g;
	($datetime = &date_time(&date_time(0))) =~ s/\:<small>.*<\/small>//g;
	open (MAIL,"|$mailprog -t") || &showErr('Webmaster Notification');
	print MAIL "To: $webmstr (Webmaster)\n";
        $vich666=wintokoi($FORM{'vizname'});
	print MAIL "From: $FORM{'email'} ($vich666)\n";
        $vc=wintokoi($listis);
	print MAIL "Subject: Addition to $vc\n\n";
	print MAIL "Local Time: $datetime\n\n";
	print MAIL "The addition from $vich666 reads:\n";
	print MAIL "  -------------------------\n";
        $vich777=wintokoi($FORM{'msg'});
	print MAIL "$vich777\n\n";
	print MAIL "  -----END Message-----\n\n";
	print MAIL "  IP Number : $ENV{'REMOTE_ADDR'}\n";
	print MAIL "  Host Server : $ENV{'REMOTE_HOST'}\n\n";
        $stroka1 = wintokoi("  Заведующий бдит зорким оком Твою страницу\n");
        $stroka2 = wintokoi("  Будь спок. дорогой товарищ. \n\n");
	print MAIL "$stroka1";
	print MAIL "$stroka2";
	close (MAIL);
}
1;