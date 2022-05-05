sub sedcoms {
	&read_rcrds; 
		my $ttl_recs = (@vizrcrds - 1);
		my $s1 = 0;
			($wrds = $FORM{'comtext'}) =~ s/(\s)*/ /g;
			$wrds =~ s/\W[^ ]/_/g;
			if ($wrds =~ /(\b\w{75,}\b)/) {&showErr('Comments Not Acceptable');}
		$FORM{'comtext'} =~ s/\cM\n/\n/gm;
		$FORM{'comtext'} =~ s/(\s)+$//;
		$FORM{'comtext'} =~ s/\n+/<br>/gm;
	for ($cnt = $ttl_recs; $cnt >= 0; $cnt--) {
		if ($vizrcrds[$cnt] =~ /^$FORM{'recnumb'}\|/) {
			@tmp = split (/\|/,$vizrcrds[$cnt]);
			$tmp[15] = "$FORM{'comtext'}\n";
			$vizrcrds[$cnt] = join ('|', @tmp); 
			$s1 = 1;
			last;
	}	}

	if (!$s1) {&showErr("Matching Record Not Found!");}
		open(RF,">$records_url") || &showErr('Records-File Write Access');
		 eval" flock(RF,2)";
			print RF @vizrcrds;
		 eval" flock(RF,8)";
		close(RF);
	if ($s1) {&noErr("Record has been updated");}
}
sub edcoms {
	my (@tmp,$tmptxt,$vizrcrds);
	open(RF,"<$records_url") || &showErr('Records-File Read Access');
	 eval" flock(RF,2)";
		while ($vizrcrds = <RF>) {
			chomp ($vizrcrds);
			@tmp = split(/\|/,$vizrcrds);
			if ($FORM{'lnmes'} eq $tmp[0]) {$cis = $tmp[2]; $tmptxt = $tmp[15]; last;}
		}
	 eval" flock(RF,8)";
	close(RF);
	if (!$tmptxt) {&showErr("Texts Not Found for<br>record # $FORM{'lnmes'}");}
	print "Content-type: text/html\n\n";
	print <<EOT;
<HTML>
<HEAD>
  <meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
  <TITLE>VizBook Records Administration</TITLE>
</HEAD>
<BODY bgcolor="#fee6cb" text="#000000" LINK="#0000FF" VLINK="#9900CC">
    <p align="center">$defont<font size="5"><b>$listis</b></font><font size="4"> Comment Editing</font><br> 
    <font size="2"><b>&#149; <A HREF="$vizAdminScrpt?frmrecs=y">Return To Admin</A> &#149;</b></FONT></P>
<FORM METHOD="POST"  action="$vizAdminScrpt" align="center">
	<input type="hidden" name="frmsedcom" value="y">
	<input type="hidden" name="recnumb" value="$FORM{'lnmes'}">
<center><table width="540" BORDER="0" CELLSPACING="0" CELLPADDING="3"><tr>
        <td align="center" width="100%" bgcolor="#D09966"><FONT FACE="arial,geneva,helvetica"><b>Comment Editing for $cis</b></FONT></td>
      </tr><tr><td bgcolor="#efefe0">
          <blockquote><p><font size="1" face="verdana, arial, geneva, helvetica">To add your own message to the visitors comment, a suggestion is to add<br>
              &quot;<font color="#990000">&lt;small&gt;&lt;br&gt;your message text&lt;/small&gt;</font>&quot;<br>
              to the end of the original texts. As administrator you can include other tags but it is wise to use them sparingly. <font color="#000099">NOTE quotes ( &quot; ) will not be accepted.</font></font></p>
          </blockquote></td></tr><tr><td bgcolor="#efefe0" align="center"><font face="arial, geneva, helvetica" size="2"><b>Note</b>: Remember to &quot;Re-Create&quot; the VizBook once returned to the admin pages</font></td>
      </tr><tr><td align="center" bgcolor="#efefe0"><FONT FACE="arial,geneva,helvetica" SIZE="2">
    	  <font color="#990000">Current Comment Texts for <b>$cis</b></font><br><textarea name="comtext" cols="60" rows="6" wrap="on">$tmptxt</textarea></FONT></td>
      </tr><tr><td align="center" width="100%" bgcolor="#C5C5C5"><FONT FACE="arial,geneva,helvetica" SIZE="2">Admin Password:</FONT><input type="password" name="admnpwd" size="12"> <input type="submit" value="Save Changes"> <input type="reset" value="Reset"></td>
      </tr></table></center></FORM><p align="center"><FONT FACE="arial,geneva,helvetica" SIZE="1">VizBook v1.56, copyright 1999 - dtp-aus.com</font></center></BODY></HTML>
EOT
exit(0);
}

1;	# this line MUST remain in all 'require' files.
