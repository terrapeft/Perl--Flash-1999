sub photos {
	&read_rcrds; 
	$ttl_recs = @vizrcrds;
		require $mailmsg;
	my $cnt = 0;
	for ($s1 = ($ttl_recs - 1); $s1 >= 0; $s1--) {
		@lrecs = split(/\|/,$vizrcrds[$s1]);
		if ($cnt < 100) {$ednmes .= "          <option value=\"$lrecs[0]\">".($cnt + 1)." $lrecs[2]</option>\n";}
		else {last;}
	$cnt++
	}
		@lrecs = "";
		foreach $s1 (@vizrcrds) {
			@lrecs = split(/\|/,$s1);
			if (!$lrecs[1]) {push(@nopic,"$lrecs[0]");}
		}
	&get_pics;
	foreach $s1 (@files) {
		foreach $s2 (@nopic) {if ($s1 =~ /$s2/) {$lst .= "      <option>$s1</option>\n";}
	}	}
	$gmtdef = sprintf("%0.2f",$gmtPlusMinus / 60 / 60);
	($dttm = &date_time_real(time + $gmtPlusMinus)) =~ s/\-/ /g;
	&get_elists;
if ($data_exten && $elists_is) {
	$radios = "
	<td valign=\"middle\" align=\"center\" colspan=\"4\" bgcolor=\"#e0e0ef\">$defont<b>This list will be saved 
	in the current \"E-Lists\" format.</b><input type=\"hidden\" name=\"elistref\" value=\"$addr_only\"></FONT></td>"; }
else {$radios = "
	<td valign=\"middle\" align=\"center\" colspan=\"1\" bgcolor=\"#e0e0ef\">$defont Address Only<br>
        <input type=\"radio\" name=\"elistref\" checked value=\"3\"></FONT></td>
	<td valign=\"middle\" align=\"center\" colspan=\"1\" bgcolor=\"#e0e0ef\">$defont Address, Name, Date<br>
        <input type=\"radio\" name=\"elistref\" value=\"\"></FONT></td>
	<td valign=\"middle\" align=\"center\" colspan=\"1\" bgcolor=\"#e0e0ef\">$defont Address, Name<br>
        <input type=\"radio\" name=\"elistref\" value=\"1\"></FONT></td>
	<td valign=\"middle\" align=\"center\" colspan=\"1\" bgcolor=\"#e0e0ef\">$defont Name, Address<br>
        <input type=\"radio\" name=\"elistref\" value=\"2\"></FONT></td>"; }
	print "Content-type: text/html\n\n";
	if (-e, "$rjctfile") {
			open(RF,"<$rjctfile") || &showErr('Reject File Read Access');
			 eval" flock(RF,2)";
				@rjcts = <RF>;
			 eval" flock(RF,8)";
			close(RF);
	}

print <<EODELS;
<HTML>
<HEAD>
  <meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
  <TITLE>VizBook Records Administration</TITLE>
</HEAD>
<BODY bgcolor="#fee6cb" text="#000000" LINK="#0000FF" VLINK="#9900CC">

<BASEFONT SIZE=2>
    <p align="center">$defont<BIG><BIG><b>Records &amp; Photos Admin for <big>$listis</big></b></BIG><br> 
     $dttm - <b>Total Records</b> = <b><font COLOR="#ff0000">$ttl_recs</font></b>.<BR> 
    <b>&#149; <A HREF="$htm_url">The Book</a> &#149; <A HREF="$vizAdminScrpt">List Defaults</A> &#149;</b></BIG></FONT></P>
EODELS

if ($allow_pics) {
print <<EODELS;
<FORM METHOD="POST" action"$vizAdminScrpt" align="center">
	<input type="hidden" name="frmadpic" value="y">
<center><table width="540" BORDER="0" CELLSPACING="0" CELLPADDING="3">
  <tr>
    <td width="100%" align="center" bgcolor="#D09966">$defont
    <b><BIG>Install New Photos</BIG></b></FONT></td> 
  </tr><tr>
    <td align="center" width="100%" bgcolor="#efefe0">$defont
    <font COLOR="#000080">To install a new picture, select an Image
    from the list and tick &quot;Install Selected&quot;</font><BR>
    Uninstalled Images found:<SELECT name="picslist">
$lst
    </SELECT>&nbsp;&nbsp;<input type="checkbox" name="instpic" value="y">:<b>Install 
    Selected</b><BR><font COLOR="#000080">This will match the image name with 
    a records ID#, and update that record.</font></FONT></td> 
  </tr><tr>
    <td align="center" width="100%" bgcolor="#C5C5C5">$defont
    Admin Password:</FONT><input type="password" name="admnpwd" size="12">&nbsp;&nbsp;<INPUT type="submit" value="Submit New Image"> <input type="reset" value="Reset"></td> 
  </tr></table></center></FORM>
EODELS
}
print <<EODELS;
<center><b>$defont <BIG>When all changes are complete, Click Here to <A HREF="$vizbkScrpt?rstfrm=y">Re-Create the HTML page</A>.</b><br><small>You might need to refresh the view to show changes.</small></BIG></font></center>
<FORM METHOD="POST" action"$vizAdminScrpt" align="center">
	<input type="hidden" name="frmdelrec" value="y">
<center><table width="540" BORDER="0" CELLSPACING="0" CELLPADDING="3">
  <tr>
    <td align="center" width="100%" bgcolor="#D09966">$defont
    <b><BIG>Remove Multiple or Single Records</BIG></b></FONT></td> 
  </tr><tr>
    <td align="center" bgcolor="#efefe0">$defont
    <font COLOR="#000080">To delete <b>MULTIPLE</b> records,
    select the month and year of the last entries<BR>you want to remove from the 
    lists and tick &quot;Delete Selected&quot;</font><BR>
    Month:<SELECT name="delmnth">
    <option value="1">01<option value="2">02
    <option value="3">03<option value="4">04
    <option value="5">05<option value="6">06
    <option value="7">07<option value="8">08
    <option value="9">09<option value="10">10
    <option value="11">11<option value="12">12
    </SELECT>&nbsp;&nbsp;Year:<SELECT name="delyr">
    <option value="1998">1998<option value="1999">1999<option value="2000">2000
    <option value="2001">2001<option value="2002">2002
    <option value="2003">2003<option value="2004">2004
    <option value="2005">2005
    </SELECT>&nbsp;&nbsp;
	<input type="radio" name="delrec" value="m">:<b>Delete Selected</b>&nbsp;&nbsp; - <font
     color="#ff0000">to AND including</font></FONT></td> 
  </tr><tr>
    <td align="center" width="100%" bgcolor="#efefe0"><hr></td>
  </tr><tr>
    <td align="center" bgcolor="#efefe0">$defont
    <font COLOR="#000080">The LAST <b>SINGLE</b> entry
    equalling the input below will be deleted.<BR>Enter the Exact Name (U/L case) and tick &quot;Delete&quot;.</font><BR>
    	Name:</FONT><input type="text" name="delname" size="30">$defont (<em>Exactly</EM>) <em>OR</em><BR>
    E-Mail Address:</FONT><input type="text" name="delmail" size="30">&nbsp;&nbsp;
	<input type="radio" name="delrec" value="s">:<b>Delete</b></td> 
  </tr><tr>
    <td align="center" width="100%" bgcolor="#C5C5C5">$defont
    	Admin Password:</FONT><input type="password" name="admnpwd" size="12">&nbsp;&nbsp;<input type="submit" value="Delete record(s)"> <input type="reset" value="Reset"></td> 
  </tr></table></center></FORM>
<FORM METHOD="POST" action="$vizAdminScrpt" align="center">
	<input type="hidden" name="frmedcom" value="y">
<center><table width="540" BORDER="0" CELLSPACING="0" CELLPADDING="3"><tr>
        <td align="center" width="100%" bgcolor="#D09966"><FONT FACE="arial,geneva,helvetica"><b>EDIT a recent &quot;Comment&quot;</b></FONT></td>
      </tr><tr align="left"><td bgcolor="#efefe0"><blockquote><p><FONT FACE="arial,geneva,helvetica" SIZE="2">
        <font size="1">With this simple option you can edit the Comments field of one of the last 100 entries by making a selection from the drop menu. The menu is in the same order as the list... last entry first.</font></FONT></p>
          </blockquote></td></tr><tr>
        <td align="center" bgcolor="#efefe0"><FONT FACE="arial,geneva,helvetica" SIZE="2"><font COLOR="#000080"></font>
    	  <select name="lnmes">$ednmes          </select>
          Select Name</FONT></td></tr><tr>
        <td align="center" width="100%" bgcolor="#C5C5C5"><FONT FACE="arial,geneva,helvetica" SIZE="2">Admin Password:</FONT><input type="password" name="admnpwd" size="12">&nbsp;&nbsp;<input type="submit" value="Edit Comment"><input type="reset" value="Clear"></td>
      </tr></table></center></FORM>
<p align="center">$defont<BIG><b>&#149; <A HREF="$htm_url">The Book</A> &#149; <A HREF="$vizAdminScrpt">List Defaults</A> &#149;</b></BIG></FONT></p>
<form method="POST" action="$vizAdminScrpt">
 	  <input type="hidden" name="rjed" value="y">
    <center><table border="0" width="540" cellspacing="0" cellpadding="2">
    <tr><td align="center" colspan="2" bgcolor="#D09966"><font face="arial,geneva,helvetica"><b>Rejection List</b></font></td></tr>
    <tr><td colspan="2" bgcolor="#efefe0"><font face="arial,geneva,helvetica" size="1"><blockquote>Two options can be included in an attempt to block repeated spamming or nuisance entries. One is to include the IP# of the offender. 
    The second is to include the email address of a person receiving email because an offender is using anothers address.<br>Note that should the offender be persistant, the webmasters e-mail receives either the IP# or host server name allowing contact with your spam complaint.</blockquote></font></td></tr>
    <tr><td valign="top" align="center" bgcolor="#efefe0" width="50%"><font face="arial,geneva,helvetica" size="2">Select <b>Item to Remove from list:</b></font><br>
      <select name="ipdel" size="1">
EODELS
foreach $r1 (sort(@rjcts)) {chomp($r1); print "        <option value=\"$r1\">$r1</option>\n"; }	
print <<EODELS;
      </select></td>
    <td valign="middle" align="center" bgcolor="#efefe0" width="50%"><font face="arial,geneva,helvetica" size="2">Enter <b>Item to Add to list:</b></font><br>
        <input type="text" name="ipad" size="30"></td></tr>
    <tr><td valign="top" align="left" bgcolor="#efefe0" colspan="2"><font face="arial,geneva,helvetica" size="2">
	  &nbsp;<input type="radio" value="d" name="iped">:<b>Delete</b> <font size="1">To Delete an IP# or E-mail Address, select it from the list and tick &quot;Delete&quot;</font><br>
	  &nbsp;<input type="radio" value="a" name="iped">:<b>Add New</b> <font size="1">To Add an IP# or E-mail Address, enter new number or address and tick &quot;Add&quot;</font></font></td></tr>
    <tr><td width="591" valign="top" align="center" colspan="2" bgcolor="#CCCCCC"><font face="arial,geneva,helvetica" size="2">admin PWrd:</font><input type="password" name="admnpwd" size="15"> <input type="submit" value="Edit Rejection List"> <input type="reset" value="Reset"></td></tr>
  </table></center></form>
<center><form method="POST" action="$vizAdminScrpt">
	<input type="hidden" name="edletta" value="y">
  <table border="0" width="540" cellspacing="0" cellpadding="2">
  <tr>
    <td width="100%" align="center" bgcolor="#D09966">$defont  <b><BIG>Edit Additional Mail Text</BIG></b></FONT></td> 
  </tr><tr>
    <td width="100%" bgcolor="#efefe0"><blockquote>$defont<small>This text is added to the start of the confirmation email sent to the persons submitting 
    new entries. Edit this text as you wish, or delete it all to use only the default texts.<br>NOTE: Use ( ' ) instead of ( &quot; ) where needed.</small></FONT></blockquote></td> 
  </tr><tr>
    <td width="100%" align="center" bgcolor="#efefe0"><textarea name="mtxt" cols="60" rows="6" wrap="off">$sndback</textarea></td>
  </tr><tr>
    <td width="100%" bgcolor="#efefe0"><blockquote>$defont<small>The text window is 60 characters wide. Use this as a guide to force wrap your lines (by hitting the ENTER 
    key near the boundary). This will ensure that your message will be easily read in most e-mail programs that use only small windows, and will appear similar to the default texts.</FONT></blockquote></td>
  </tr><tr>
	<td width="100%" align="center" bgcolor="#C5C5C5">$defont Admin Password:</FONT><input type="password" name="admnpwd" size="12"> <input type="submit" value="Save Changes"> <input type="reset" value="Reset"></td>
</tr></table></form></center>
<center><form method="POST" action="$vizAdminScrpt">
	<input type="hidden" name="aped" value="y">
  <table border="0" width="540" cellspacing="0" cellpadding="2">
  <tr>
    <td width="100%" align="center" colspan="3" bgcolor="#D09966">$defont
    <b><BIG>Change Admin Password</BIG></b></FONT></td> 
  </tr><tr>
    <td width="33%" align="center" bgcolor="#efefe0">$defont<b>OLD</b> Admin password:</FONT><br>
      <input type="password" name="admnpwd" size="12"></td>
      <td width="33%" align="center" bgcolor="#efefe0">$defont<b>NEW</b> Admin Password:</FONT><br>
      <input type="password" name="newpwrd1" size="12"></td>
      <td width="33%" align="center" bgcolor="#efefe0">$defont Repeat <b>NEW</b>:</FONT><br>
      <input type="password" name="newpwrd2" size="12"></td>
  </tr><tr>
	<td width="100%" valign="top" align="center" colspan="3" bgcolor="#C5C5C5"><input type="submit" value="Change ADMIN Password"> <input type="reset" value="Reset"></td>
</tr></table></form></center>
<center><form method="POST" action="$vizAdminScrpt">
 	<input type="hidden" name="gmed" value="y">
   <table border="0" width="540" cellspacing="0" cellpadding="2">
  <tr>
    <td width="100%" align="center" colspan="2" bgcolor="#D09966">$defont <b><BIG>Adjust GMT time zone</BIG></b></FONT></td> 
  </tr><tr>
	<td valign="middle" align="center" nowrap bgcolor="#efefe0">$defont<b>&nbsp;GMT</b></FONT><br>
      &nbsp;&nbsp;<input type="text" name="gmt" value="$gmtdef" size="8">&nbsp;&nbsp;$defont<br>Hours + or -</FONT></td>
      <td bgcolor="#efefe0">$defont<SMALL><font color="#000080">If you move from the current time zone, or change to / from daylight savings, enter the 
	new value and submit. Even if your local GMT time zone equals the servers, you must
      have your local GMT time zone value entered here.</font></SMALL> (ie 5.5 or -9 etc)</FONT></td>
  </tr><tr>
	<td width="100%" valign="top" align="center" colspan="2" bgcolor="#C5C5C5">$defont Admin Password:</FONT><input type="password" name="admnpwd" size="12"> <input type="submit" value="Change GMT Zone"> <input type="reset" value="Reset"></td>
</tr></table></form></center>
<center><form method="POST" action="$vizAdminScrpt">
	<input type="hidden" name="dbref" value="y">
   <table  border="0" width="540" cellspacing="0" cellpadding="2">
    <tr><td width="100%" align="center" bgcolor="#D09966">$defont<b><BIG>Create DB File</BIG></b></FONT></td>
    </tr><tr>
      <td valign="middle" align="center" bgcolor="#e0e0ef">$defont<font
      color="#000080">The ( | ) delimited DB file, with header, will be created in your data files directory<br>and 
      overwrite any previous file - see Readme.html.</font></FONT></td>
    </tr><tr>
      <td valign="middle" align="center" bgcolor="#e0e0ef">$defont
	  <input type="checkbox" name="addquot" value="y">:<b>Include Quotes</b> ie (&quot;|&quot;Bart&quot;|&quot;Simpsons&quot;|&quot;)</FONT></td>
    </tr><tr>
      <td width="100%" valign="top" align="center" bgcolor="#C5C5C5">$defont Admin Password:</FONT><input type="password" name="admnpwd" size="12"> <input type="submit" value="Create DataBase file"> <input type="reset" value="Reset"></td>
    </tr></table></form></center>
<center><form method="POST" action="$vizAdminScrpt">
 	<input type="hidden" name="makemail" value="y">
   <table border="0" width="540" cellspacing="0" cellpadding="2">
  <tr>
    <td width="100%" align="center" colspan="4" bgcolor="#D09966">$defont
    <b><BIG>Create an E-Mail List</BIG>$elists_is</b></FONT></td> 
  </tr><tr>
$radios
  </tr><tr>
	<td valign="middle" align="center" colspan="4" bgcolor="#e0e0ef">$defont<font color="#000080">The e-mail 
	list will be created in your data files directory - see Readme.html.</font></FONT></td>
  </tr><tr>
	<td valign="middle" align="center" colspan="4" bgcolor="#e0e0ef">$defont<input type="radio" name="appnd" checked value="y">:<b>Update</b> Previous 
	<input type="radio" name="appnd" value="n">:<b>Overwrite</b> Previous</FONT></td>
  </tr><tr>
	<td width="100%" valign="top" align="center" colspan="4" bgcolor="#C5C5C5">$defont Admin Password:</FONT><input type="password" name="admnpwd" size="12"> <input type="submit" value="Create E-Mail List"> <input type="reset" value="Reset"></td>
</tr></table></form></center>
<p align="center"><font face="arial,geneva,helvetica" size="1">VizBook v1.56, copyright 1999 - dtp-aus.com</font></center>
</BODY></HTML>
EODELS
}
sub do_elist {
	&get_elists;
		if ($elists_is) {$elist_dir .= "vbkelist$data_exten";}
		else {$elist_dir .= "vbkelist.m";}
	&read_rcrds; 
		local(@elist_in);
		if (! -e "$elist_dir") {
			open(EL,">>$elist_dir") || &showErr('Cannot Create Mail-List File');
			close(EL);		}
		elsif ($FORM{'appnd'} eq "y") {open(EL,"<$elist_dir") || &showErr('Mail-List File Read Access');
			 eval" flock(EL,2)";
	 			@elist_in = <EL>;
			 eval" flock(EL,8)";
			close(EL);		}
	$s6 = 0;
	foreach $s1 (@vizrcrds) {
		$s5 = 0;
		(@tmp) = split(/\|/,$s1);
		($s2,$s3,$s4) = @tmp[2,3,14];
		$s2 =~ /^([^ ]*)(.*) /;
		if (length($1) > 1 && $1 !~ /\./) {$s2 = $1;}
	if ($addr_only eq "1") {$recout = "$s3,$s2\n";}
	elsif ($addr_only eq "2") {$recout = "$s2,$s3\n";}
	elsif ($addr_only eq "3") {$recout = "$s3\n";}
	else {$recout = "$s3,$s2,".&date_time_real($s4)."\n";}
		if ($FORM{'appnd'} eq "n") {push(@elist_in,$recout); $s6++;}
		else {
			foreach $tmp (@elist_in) { if ($tmp =~ /$s3/i) {$s5 = 1;}  }
			if (!$s5) {push(@elist_in,$recout); $s6++;}
	}	}
	open(EL,">$elist_dir") || &showErr('Mail-List File Write Access');
		 eval" flock(EL,2)";
			print EL sort(@elist_in);
		 eval" flock(EL,8)";
		close(EL);
	&noErr("$s6 Record(s) Added to Mail-List");
}
sub instpic {
if ($FORM{'instpic'} ne "y") {&showErr('Please Confirm Action with Check Box');}
	&read_rcrds; 
	$s3 = 0;
if ($FORM{instpic}) {
	open(RF,">$records_url") || &showErr('Records-File Write Access');
	 eval" flock(RF,2)";
($pic = $FORM{picslist}) =~ s/(\.gif|.jpg)//gi;
for ($s1 = 0; $s1 < @vizrcrds; $s1++) {
	@tmp = split(/\|/,@vizrcrds[$s1]);
	if (@tmp[0] eq $pic) {
		@tmp[13] = $FORM{picslist};
		@tmp[1] = 1;
		@vizrcrds[$s1] = "";
		foreach $s2(@tmp) {@vizrcrds[$s1] .= "$s2|";}
		@vizrcrds[$s1] =~ s/\|$//g;
		$s3 = 1;
}	}
		print RF @vizrcrds;
	 eval" flock(RF,8)";
	close(RF);
}
	if ($s3 eq 0) {&showErr('Record ID# Match Not Found!');}
	elsif ($s3 eq 1) {&noErr('ID# Found, Image Data Installed');}
}
sub delrecs {
	&read_rcrds; 
	$s2 = 0; $s3 = 0;
if ($FORM{'delrec'} eq "m") {
	open(RF,">$records_url") || &showErr('Records-File Write Access');
	 eval" flock(RF,2)";
	for ($s1 = @vizrcrds -1; $s1 >= 0; $s1--) {
		@tmp = split(/\|/,@vizrcrds[$s1]);
		($mnth,$year) =  &date_time(@tmp[14]);
		if ($mnth eq $FORM{'delmnth'} && $year eq $FORM{'delyr'}) {splice(@vizrcrds,$s1,1); $s2 = 1; $s3++;}
	}
		print RF @vizrcrds;
	 eval" flock(RF,8)";
	close(RF);
	if ($s2 eq 0) {&showErr('No Matching Records Found!');}
	elsif ($s2 eq 1) {&noErr("$s3 Record(s) Found and Deleted");}
}
elsif ($FORM{'delrec'} eq "s") {
	open(RF,">$records_url") || &showErr('Records-File Write Access');
	 eval" flock(RF,2)";
	for ($s1 = @vizrcrds -1; $s1 >= 0; $s1--) {
		@tmp = split(/\|/,@vizrcrds[$s1]);
		if (@tmp[2] eq $FORM{'delname'} || ($FORM{'delmail'} && @tmp[3] eq $FORM{'delmail'})) {
			$s3++;
			if ($s2 eq 0) {splice(@vizrcrds,$s1,1); $s2++;}
		}
	}
		print RF @vizrcrds;
	 eval" flock(RF,8)";
	close(RF);
	if ($s2 eq 0) {&showErr('No Matching Record Found!');}
	elsif ($s2 eq 1) {&noErr("$s3 Matching Record(s) Found, $s2 Deleted");}
}
else {&showErr('Please Confirm Choice via Radio Buttons');}
}
sub dodb {
	&read_rcrds; 
for ($s1=0;$s1<@vizrcrds;$s1++) {
	@tmp = split(/\|/,@vizrcrds[$s1]);
	$s2 = &date_time_real(@tmp[14]);
	($s3,$s4) = split(/\-/,$s2);
	if (@tmp[9]) {@tmp[8] = @tmp[9];}
		chomp(@tmp[15]);
		@tmp[15] =~ s/\&amp\;/\&/g;
		@tmp[15] =~ s/\&quot\;/\'/g;
		@tmp[15] =~ s/\&lt\;/</g;
		@tmp[15] =~ s/\&gt\;/>/g;
		@tmp[15] =~ s/<br>/  /g;
	@vizrcrds[$s1] = "$s3|$s4|@tmp[2]|@tmp[3]|@tmp[4]|@tmp[5]|@tmp[6]|@tmp[7]|@tmp[8]|@tmp[10]|@tmp[11]|@tmp[12]|@tmp[15]";
		if ($FORM{'addquot'} eq "y") {
			@vizrcrds[$s1] =~ s/\|/\"\|\"/g; 
			@vizrcrds[$s1] = "\"".@vizrcrds[$s1]."\"";
		}
		@vizrcrds[$s1] .= "\n"; 
}
	$heada = "Dte|Tme|Nme|EMail|ICQ|Cmpny|URL|Msc1|Msc2|Cty|Stte|Cntry|Msg";
	if ($FORM{'addquot'} eq "y") {
		$heada =~ s/\|/\"\|\"/g; 
		$heada = "\"".$heada."\"";
	}
	$heada .= "\n"; 
	unshift(@vizrcrds,$heada);
			$fn = "DBfile.t";
		open(DB,">$elist_dir$fn") || &showErr('DB-File Write Access');
		 eval" flock(DB,2)";
			print DB @vizrcrds;
		 eval" flock(DB,8)";
		close(DB);
	&noErr("DB File of $s1 records Created");
}
sub new_pwrd {
	if ($FORM{'newpwrd1'} ne $FORM{'newpwrd2'}) {&showErr('New ADMIN Password Entries Do Not Match');}
	elsif ($FORM{'newpwrd1'} eq $FORM{'adminspwrd'}) {&showErr('No Change Requested');}
	@theAword[1] = crypt($FORM{'newpwrd1'},"sf");
		open(ADMwrd, ">$adminword_url") || &showErr('ADMIN Password File Access');
 		 eval" flock (ADMwrd,2)";
			print ADMwrd @theAword;
		 eval" flock (ADMwrd,8)";
		close(ADMwrd);
		&noErr('New ADMIN Password Installed');
}
sub new_gmt {
	if ($FORM{'gmt'} !~ /[0-9]/) {&showErr('GMT Value Error');}
	elsif ($FORM{'gmt'} > 12 || $FORM{'gmt'} < -12) {&showErr('GMT <> + or - 12');}
		$s1 = "\$gmtPlusMinus = ".($FORM{'gmt'} * 60 * 60).";\n";
	open (GMT, "<$gmt_url") || &showErr('GMT.SET File Access');
 	 eval" flock (GMT,2)";
		@gmtin = <GMT>;
 	 eval" flock (GMT,8)";
	close (GMT);
		$cnts = 0; $s3 = 0;
		foreach $s2 (@gmtin) {
			if ($s2 =~ /gmtPlusMinus/) {@gmtin[$cnts] = $s1; $s3 = 1; next;}
		$cnts++;
		}
		if ($s3 eq 0) {&showErr('gmt.set Variable Not Found');}
	open (GMT, ">$gmt_url") || &showErr('GMT.SET File Access');
 	 eval" flock (GMT,2)";
		print GMT @gmtin;
 	 eval" flock (GMT,8)";
	close (GMT);
	&noErr('New GMT Value is set');
}
sub rjcted {
if ($FORM{'rjed'} eq "y") {
	if (-e, "$rjctfile") {
		open(RF,"<$rjctfile") || &showErr('Reject File Read Access');
		 eval" flock(RF,2)";
			@rjcts = <RF>;
		 eval" flock(RF,8)";
		close(RF);
	}

	if ($FORM{iped} eq "a") {
		if ($FORM{ipad} !~ /[a-zA-Z0-9]/) {&showErr('New Entry Error');}
		$FORM{ipad} =~ tr/[A-Z]/[a-z]/;
		$s2 = 0;
		foreach $s1 (@rjcts) {
			chomp($s1);
			if ($s1 eq $FORM{'ipad'}) {$s2 = 1; next;}
		}	
		if ($s2) {&showErr('Entry Already Exists');}
			open(RF,">>$rjctfile") || &showErr('Reject File Write Access');
			 eval" flock(RF,2)";
				print RF "$FORM{'ipad'}\n";
			 eval" flock(RF,8)";
			close(RF);
		&noErr('New Reject Entry Added');
	}
	elsif ($FORM{iped} eq "d") {
		if ($FORM{'ipdel'} !~ /[a-zA-Z0-9]/) {&showErr('Nothing Selected');}
		$FORM{ipdel} =~ tr/[A-Z]/[a-z]/;
		$s2 = 0;
		for($s1 = 0; $s1 < @rjcts; $s1++) {
			$s3 = @rjcts[$s1];
			chomp($s3);
			if ($s3 eq $FORM{'ipdel'}) {splice(@rjcts, $s1, 1); $s2 = 1; next;}
		}
		if (!$s2) {&showErr('Matching Entry Not Found');}
			open(RF,">$rjctfile") || &showErr('Reject File Write Access');
			 eval" flock(RF,2)";
				print RF @rjcts;
			 eval" flock(RF,8)";
			close(RF);
		&noErr('Reject Entry Removed');
	}
	else {&showErr('No ADD or DELETE confirmation');}
}
}
sub edlet {
	$FORM{'mtxt'} =~ s/\"/'/g;
	$FORM{'mtxt'} =~ s/(\n|\r)*$//g;
		open(TF,">$mailmsg") || &showErr('Text File Write Access');
		 eval" flock(TF,2)";
		 	print TF "# DO NOT EDIT. USE THE ADMIN OPTION ONLY\n";
		 	print TF "\$sndback = \"$FORM{'mtxt'}\n\n\";\n";
			print TF "1;\n";
		 eval" flock(TF,8)";
		close(TF);
	&noErr("The text file has been updated");
}
1;	# this line MUST remain in all 'require' files.
