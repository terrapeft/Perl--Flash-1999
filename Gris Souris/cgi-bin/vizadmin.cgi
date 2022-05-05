#! /usr/bin/perl

#   Welcome to the www.dtp-aus.com VizBook scripts. VERSION 1.56 Oct.1999    #
# IMPORTANT INFORMATION THAT MUST BE READ IF YOU WISH TO USE THESE SCRIPTS   #
##############################################################################
# The scripts "VIZBOOK.CGI" and "VIZADMIN.CGI were written (and (c)) by Ron  #
# F Woolley, Melbourne Australia. Copyright 1998. These scripts CAN NOT BE   #
# ALTERED for personal use except as instructed here in, NOR can whole or    #
# portions of code be copied, AND all of the header notices in the scripts   #
# MUST REMAIN intact as is, AND, using the scripts without first reading the #
# README file(s), is prohibited. IF YOU DO NOT AGREE, destroy all files NOW! #
#     These scripts must not be sold or given/made available to others.      #
#                                                                            #
# Australian copyright is recognised/supported in over 130 countries...      #
# per the Berne Convention (including USA!)                                  #
#                                                                            #
#  The scripts and associated files remain the property of Ron F Woolley.    #
#  NO PROFIT what so ever is to be gained from users of these scripts for    #
#  the use of these scripts, except that a reasonable minimal charge for     #
#  installation may be allowed if installing, as a site developer, for a     #
#  user on the users site that is not on the developers site. This program   #
#  must NOT be used for multiple VizBook users on one site OR offered as a   #
#  remote service.                                                           #
#                                                                            #
#  Ron Woolley, the author, MUST be notified via the addresses/URLs below    #
#  if any gain is to be made from the installation of these scripts.         #
#                                                                            #
#  You MUST RETAIN the small identifying text line at the base of each page  #
#          IF YOU DISAGREE, you must immediately destroy all files.          #
##############################################################################
# NOTE: If you use these files, you do so entirely at your own risk, and     #
# take on full responsibility for the consequences of using the described    #
# files. You must first agree that Ron Woolley / HostingNet, the ONLY        #
# permitted suppliers of this or accompanying files are exempt from any      #
# responsibility for all or any resulting problems, losses or costs caused   #
# by your using these or any associated files.                               #
# IF YOU DISAGREE, you must immediately destroy all files.                   #
##############################################################################
#  These program scripts are free to use, but if you use them, a donation of #
# of A$25.00 would be appreciated and help in continuing support for VizBook #
# and the creation of other scripts for users of the internet.               #
# Secure On-Line payments can be made for support donations or installations #
##############################################################################
# Support Information is available at:                                       #
# http://www.dtp-aus.com/cgiscript/scrpthlp.htm                              #
# Files from:                                                                #
# http://www.dtp-aus.com/cgiscript/vizbook.shtml                             #
#                                                                            #
#  THESE FILES can only be obtained via the above web addresses, and MUST    #
#  NOT BE PASSED ON TO OTHERS in any form by any means what so ever.         #
#           This does not contradict any other statements above.             #
##############################################################################

#--- Alter these two paths only, if needed! ---------------------#
	require "sets/vizbkset.pl";
	require "sets/gmtset.pl";
#--- Do Not make any changes below this line. -------------------#

	&check_method;
		&check_ref ;
	@pairs = split(/&/, $query_string);
	foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$name =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ s/~!/ ~!/g;
		$name =~ s/~!/ ~!/g;
		$value =~ s/<([^>]|\n)*>//g if $name ne "comtext"; 
		$name =~ s/<!--#(.|\n)*-->//g;
		$value =~ s/<!--#(.|\n)*-->//g;
		$value =~ s/("|'|`|\0|\\)//g;
		$name =~ s/("|'|`|\0|\\)//g;
	$FORM{$name} = $value;
	}
	if (!$tbl_wid) {$tbl_wid = "590";} else {$tbl_wid = "95%";}
	if (!$sze_3) {$sze_3 = 2;}
	else {$sze_3 = 3;}
	$defont = "<FONT FACE=\"arial,geneva,helvetica\" SIZE=\"-1\">";

	if ($FORM{'frmedit'} eq "y") {&admn_pwrd; &set_defaults;}
	elsif ($FORM{'frmdelrec'} eq "y") {require $edit_form; &admn_pwrd; &delrecs;}
	elsif ($FORM{'frmadpic'} eq "y") {require $edit_form; &admn_pwrd; &instpic;}
	elsif ($FORM{'aped'} eq "y") {require $edit_form; &admn_pwrd; &new_pwrd;}
	elsif ($FORM{'gmed'} eq "y") {require $edit_form; &admn_pwrd; &new_gmt;}
	elsif ($FORM{'makemail'} eq "y") {require $edit_form; &admn_pwrd; &do_elist;}
	elsif ($FORM{'rjed'} eq "y") {require $edit_form; &admn_pwrd; &rjcted;}
	elsif ($FORM{'edletta'} eq "y") {require $edit_form; &admn_pwrd; &edlet;}
	elsif ($FORM{'frmrecs'} eq "y") {require $edit_form; &photos;}
	elsif ($FORM{'frmedcom'} eq "y") {require $edcom; &admn_pwrd; &edcoms;}
	elsif ($FORM{'frmsedcom'} eq "y") {require $edcom; &admn_pwrd; &sedcoms;}
	elsif ($FORM{'dbref'} eq "y") {require $edit_form; &admn_pwrd; &dodb;}
	else {&shw_samp;}
exit(0);

sub check_method {
	if ( $ENV{'REQUEST_METHOD'} eq 'GET' ) { $query_string = $ENV{'QUERY_STRING'}; } 
  	elsif ( $ENV{'REQUEST_METHOD'} eq 'POST' ) { read(STDIN,$query_string,$ENV{'CONTENT_LENGTH'}); }
	else { &showErr('Request Method'); }
}
sub check_ref {
	$crf = 0;
	if ($ENV{'HTTP_REFERER'}) {
        foreach $referer (@referers) {
            if ($ENV{'HTTP_REFERER'} =~ m|\Ahttps?://([^/]*)$referer|i) {
                $crf = 1;
                last;
            }  }
	}
}
sub read_rcrds {
	open(RF,"<$records_url") || &showErr('Records-File Read Access');
	 eval" flock(RF,2)";
		@vizrcrds = <RF>;
	 eval" flock(RF,8)";
	close(RF);
}
sub admn_pwrd {
if (!( -e "$adminword_url")) {open(FF,">>$adminword_url") || &showErr('Missing ADMIN Password File'); print FF "Do NOT Edit\n"; close(FF);}
	open(ADMwrd, "<$adminword_url") || &showErr('ADMIN Password File Access');
 	 eval" flock (ADMwrd, 2)";
		@theAword = <ADMwrd>;
	 eval" flock (ADMwrd, 8)";
	close(ADMwrd);
	if ($theAword[1] || $FORM{'admnpwd'}) {
		if (crypt($FORM{'admnpwd'},"sf") ne $theAword[1]) {&showErr('Incorrect ADMIN Password');}
	}
}
sub shw_samp {
	&read_rcrds; 
	$per_page = 35 if $per_page eq 0;
	$ttl_recs = @vizrcrds;
	print "Content-type: text/html\n\n";

print <<EOTOP;
<html>
<head>
  <meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
<title>VizBook Administration</title>
</head>
<body background="$admn_picsdir/$bk_bgimg" bgcolor="$bk_bgcolr" text="$bk_text" link="$bk_lnk" vlink="$bk_vlnk" alink="#FF0000">
<BASEFONT size=2>
  <center><table border="0" cellpadding="2" cellspacing="0" $tb_tbleclr width="590">
  <tr><td width="100%" colspan="1" align="center">$defont<strong>Personalising Page for</strong></FONT></td></tr>
  <tr><td width="100%" colspan="1" align="center" $tb_cellclr><strong><font size="6" color="$misc_clr">$listis</font></strong>.</td></tr>
  <tr><td width="100%" colspan="1" align="center"><font size="2"><strong>Total Records</strong> = <font color="$misc_clr"><strong>$ttl_recs</strong></font>. <strong>Records Viewed Per Page</strong> = <font color="$misc_clr"><strong>$per_page</strong></font>.</td></tr>
  </table>
  $defont<BIG><strong><a href="$htm_url">The Book</a> &#149; <a href="$vizAdminScrpt?frmrecs=y">Records and Photos</a> &#149;</strong></BIG></FONT>
 <table border="0" cellpadding="3" cellspacing="0" width="$tbl_wid">
  <tr><td width="100%" colspan="2" align="center"><font size="$sze_3" face="$pref_fnt">
  </font></td></tr><tr><td width="100%" colspan="2"><hr noshade size="1"></td></tr>
EOTOP
$i3 = "Wally Farnarkle"; $i4 = "abody\@abc.def"; $i5 = "00000000"; $i6 = "Bloggs Bicycles"; $i7 = "http://www.nowhere.net/"; $i8 = "Whatever";
$i9 = "Where ever"; $i10 = "Where ever"; $i11 = "City"; $i12 = "State"; $i13 = "Country"; $i14 = "admn.gif"; $i15 = "60"; $i16 = "60"; $i17 = "Mon 26 Oct 1998 - 09:58:<small>35</small> am"; $i18 = "This is a sample view of current options showing you the results of text, background colours, fonts and table widths. Make changes to the form below and click 'Submit Changes' to view an updated sample.";
    print " <tr><td width=\"70\" align=\"right\" nowrap valign=\"top\"><font size=\"$sze_3\" face=\"$pref_fnt\">\n";
    print "   <strong>Name:<br>\n";
    if ($shw_cmpny && $i6) {print "   Company:<br>\n";}
    if ($shw_city && $i11) {print "   From:<br>\n";}
    if ($list_miscbox && $shw_miscbox && $i8) {print "   $miscbox_txt:<br>\n";}
    if ($list_drpdwn && $shw_drpdwn && ($i9 || $i10)) {print "   $drpdwn_txt:<br>\n";}
    print "   Date:</strong></font></td>\n";
    print " <td valign=\"top\" align=\"left\" $nme_cellclr width=\"98%\"><font size=\"$sze_3\" face=\"$pref_fnt\">\n";
	$href = $i3;
    if ($shw_url && $i7) {$href = "<a href=\"$i7$blnk\">$i3</a>";}
    print " $href";
if ($list_email) {
    print "&nbsp;&nbsp;&nbsp;<strong>Email:</strong> <a HREF=\"mailto:$i4\">$i4</a>";
    if ($shw_icq && $i5) {print "&nbsp;&nbsp;&nbsp;<strong>ICQ#:</strong> <a href=\"http://wwp.mirabilis.com/$i5$blnk\">$i5</a>";} 
}
    print "<br>\n";
    if ($shw_cmpny && $i6) {print "   $i6<br>\n";}
    if ($shw_city && $i11) {print "   $i11, $i12 $i13<br>\n";}
    if ($list_miscbox && $shw_miscbox && $i8) {print "   $i8<br>\n";}
    if ($list_drpdwn && $shw_drpdwn && ($i10 || $i9)) {
		if ($i10) {print "   $i10<br>\n";}
		else {print "   $i9<br>\n";}
    }
    print "   $i17</font></td>\n";
    print " </tr><tr>\n";
    print " <td width=\"70\" align=\"center\" valign=\"top\">\n";
    if ($allow_pics) {print "  <img src=\"$admn_picsdir/admn.gif\" width=\"60\" height=\"60\" border=\"0\">";}
    print " </td>\n";
    print " <td valign=\"top\" align=\"left\" width=\"98%\" $msg_cellclr><font size=\"$sze_3\" face=\"$pref_fnt\">\&#149;\&nbsp;\&nbsp;\&nbsp;\n";
    print "   $i18</font></td></tr>\n";
    print " <tr><td width=\"70\"></td><td align=\"center\"";
	if ($use_divider) {print " ><img src=\"$admn_picsdir/$divider\" align=\"middle\" width=\"$dvdr_wid\" height=\"$dvdr_hgt\" border=\"0\">";}
	else {print " $nme_cellclr><hr width=\"100%\">";}
    print "</td></tr>\n";
    print " <tr><td width=\"100%\" colspan=\"2\"><hr noshade size=\"1\"></td></tr>\n";
    print " <tr><td width=\"100%\" colspan=\"2\" align=\"center\"><font size=\"$sze_3\" face=\"$pref_fnt\">$views</font></td></tr>\n";
    print "</table></center>\n";

	&get_pics;
		$lst .= "      <option></option>\n";
		$lst1 .= "      <option></option>\n";
		$lst2 .= "      <option></option>\n";
	foreach $s1 (@files2) {
		if ($s1 eq $bk_bgimg) {$lst .= "      <option selected>$s1</option>\n";}
		else {$lst .= "      <option>$s1</option>\n";}
		if ($s1 eq $add_bgimg) {$lst1 .= "      <option selected>$s1</option>\n";}
		else {$lst1 .= "      <option>$s1</option>\n";}
		if ($s1 eq $divider) {$lst2 .= "      <option selected>$s1</option>\n";}
		else {$lst2 .= "      <option>$s1</option>\n";}
	}

print <<EOADMN;
<center>$defont<BIG><strong> When all changes are completed, Click Here to <A HREF="$vizbkScrpt?rstfrm=y">Re-Create the HTML page</A>.</strong><br><small>You might need to refresh the view to show changes.</small></BIG></FONT></center>
<form method="POST" action="$vizAdminScrpt">
    <input type="hidden" name="frmedit" value="y">
<center><table width="590" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="8" align="center" bgcolor="#CCCCCC">$defont
     <BIG><strong><font color="#000000">List Appearance</font></strong></BIG></FONT></td>
  </tr><tr>
    <td width="50%" colspan="4" align="center" $msg_cellclr>$defont List Background Image<br>
    <SELECT name="lstbgimg">
$lst    </select>
    </FONT></td>
    <td width="50%" colspan="4" align="center" $msg_cellclr>$defont Add-Form Background Image<br>
    <SELECT name="addbgimg">
$lst1    </select>
    </FONT></td>
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr><hr></td>
  </tr><tr>
    <td align="center" $msg_cellclr colspan="2" width="25%">$defont
    Items Per Page:<input name="perpge" type="text" size="3" value="$per_page" maxlength="3"></FONT></td>
    <td align="center" $msg_cellclr colspan="2" width="25%">$defont
    Table: 590<input type="radio" value="0" name="tblwid" 
EOADMN
if ($tbl_wid eq 590) {print "    checked> 95%<input type=\"radio\" value=\"1\" name=\"tblwid\"></FONT></td>\n";}
else {print "    > 95%<input type=\"radio\" value=\"1\" name=\"tblwid\" checked></FONT></td>\n";}
	$tmp = ""; $tmp = "checked" if $shw_url;      
	$tmp2 = ""; $tmp2 = "checked" if $shw_cmpny;      
	$tmp3 = ""; $tmp3 = "checked" if $shw_city;      
	$tmp4 = ""; $tmp4 = "checked" if $list_email;      
print <<EOADMN;
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    Use URL:<input type="checkbox" name="shwurl" $tmp value="1"></FONT></td>
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    Use Company:<input type="checkbox" name="shwcomp" $tmp2 value="1">&nbsp;</FONT></td>
  </tr><tr>
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    Use City:<input type="checkbox" name="shwcty" $tmp3 value="1"></FONT></td>
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    List E-Mail:<input type="checkbox" name="lstmail" $tmp4 value="1"></FONT></td>
EOADMN
	$tmp = ""; $tmp = "checked" if $shw_icq;      
	$tmp2 = ""; $tmp2 = "checked" if $list_miscbox;      
	$tmp3 = ""; $tmp3 = "checked" if $list_drpdwn;      
print <<EOADMN;
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    Use ICQ#:<input type="checkbox" name="shwicq" $tmp value="1"></FONT></td>
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    List Misc Box:<input type="checkbox" name="lstmisc" $tmp2 value="1">&nbsp;</FONT></td>
  </tr><tr>
    <td align="right" $msg_cellclr colspan="2" width="25%">$defont
    List DropDown:<input type="checkbox" name="lstmnu" $tmp3 value="1"></FONT></td>
    <td align="center" $msg_cellclr colspan="6" width="75%">$defont
    Font Name:<input name="fname" type="text" size="25" value="$pref_fnt"> Size: 2<input 
EOADMN
	if ($sze_3 eq 3){print"    type=\"radio\" name=\"fsize\" value=\"0\"> 3<input type=\"radio\" value=\"1\" name=\"fsize\" checked></FONT></td>\n";}
	else {print"    type=\"radio\" name=\"fsize\" value=\"0\" checked> 3<input type=\"radio\" value=\"1\" name=\"fsize\"></FONT></td>\n";}
	$tmp = ""; $tmp = "checked" if $use_divider;      
	($tmp1 = $nme_cellclr) =~ s/(^.+"#|"$)//g;
	($tmp2 = $msg_cellclr) =~ s/(^.+"#|"$)//g;
	($tmp3 = $tb_tbleclr) =~ s/(^.+"#|"$)//g;
	($tmp4 = $tb_cellclr) =~ s/(^.+"#|"$)//g;
print <<EOADMN;
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr><hr></td>
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr>$defont
    Use Divider :<input type="checkbox" name="usediv" $tmp value="1">
    Image Name:<SELECT name="divname">
$lst2    </select> 
 width:<input name="divwid" type="text" size="3" value="$dvdr_wid"> height:<input name="divhgt" 
    type="text" size="2" value="$dvdr_hgt"></FONT></td>
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr><hr></td>
  </tr><tr>
    <td align="center" $msg_cellclr width="23%">$defont Background Colour<br>
    <input name="bgclr" type="text" size="8" value="$bk_bgcolr"></FONT></td> 
    <td align="center" bgcolor="$bk_bgcolr" width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td> 
    <td align="center" $msg_cellclr width="23%">$defont Text Colour<br>
    <input name="txtclr" type="text" size="8" value="$bk_text"></FONT></td> 
    <td align="center" bgcolor="$bk_text" width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td>
    <td align="center" $msg_cellclr width="23%">$defont Link Colour<br>
    <input name="lnkclr" type="text" size="8" value="$bk_lnk"></FONT></td> 
    <td align="center" bgcolor="$bk_lnk" width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td>
    <td align="center" $msg_cellclr width="23%">$defont Visited Link Colour<br>
    <input name="vlnkclr" type="text" size="8" value="$bk_vlnk"></FONT></td> 
    <td align="center" bgcolor="$bk_vlnk" width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td>
  </tr><tr>
    <td align="center" $msg_cellclr width="23%">$defont Name Panel Colour<br>
    <input name="namesclr" type="text" size="8" value="#$tmp1"></FONT></td> 
    <td align="center" $nme_cellclr width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td> 
    <td align="center" $msg_cellclr width="23%">$defont Msg Panel Colour<br>
    <input name="msgclr" type="text" size="8" value="#$tmp2"></FONT></td> 
    <td align="center" $msg_cellclr width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td>
    <td align="center" $msg_cellclr width="23%">$defont Top Table Colour<br>
    <input name="tblclr" type="text" size="8" value="#$tmp3"></FONT></td> 
    <td align="center" $tb_tbleclr width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td>
    <td align="center" $msg_cellclr width="23%">$defont Top Cell Colour<br>
    <input name="celclr" type="text" size="8" value="#$tmp4"></FONT></td> 
    <td align="center" $tb_cellclr width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td>
  </tr><tr>
    <td align="center" $msg_cellclr width="23%">$defont Misc. Colour<br>
    <input name="mscclr" type="text" size="8" value="$misc_clr"></FONT></td> 
    <td align="center" bgcolor="$misc_clr" width="2%">$defont&nbsp;&nbsp;&nbsp;</FONT></td> 
    <td colspan="6" align="center" $msg_cellclr width="75%">$defont
EOADMN
	$tmp = ""; $tmp = "checked" if $shw_miscbox;      
print <<EOADMN;
    Use Misc Box:<input type="checkbox" name="usemisc" $tmp value="1">
    Box Caption:<input name="misccapt" type="text" size="12" value="$miscbox_txt"> box
    width:<input name="mscwid" type="text" size="2" value="$miscbox_wid"></FONT></td>
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr><hr></td>
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr>$defont
EOADMN
	$tmp = ""; $tmp = "checked" if $shw_drpdwn;      
print <<EOADMN;
    Use DropDown Menu:<input type="checkbox" name="usemnu" $tmp 
    value="1"> Menu Caption:<input name="mnucapt" type="text" size="12" value="$drpdwn_txt">
    &quot;Other&quot; box width:<input name="othrwid" type="text" size="2" value="$droptxt_wid"><br>
    List Items:<SELECT name="mnuitms">
EOADMN
	foreach $s1 (@dropdwn_items) {print "	  <option>$s1</option>\n";}
print <<EOADMN;
    </SELECT> Add New Item:<input type="text" name="aditem" size="20"><br>
    Add:<input type="radio" name="mnuadd" value="a">
    Delete:<input type="radio" name="mnuadd" value="d"> <SMALL>To Add or
    Delete, select one or enter it in the box above. Then click 'Add' or 'Delete'.</SMALL></FONT></td>
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr><hr></td>
  </tr><tr>
EOADMN
	$tmp = ""; $tmp = "checked" if $allow_pics;      
	$tmp1 = ""; $tmp1 = "checked" if $topbanna;      
	$tmp2 = ""; $tmp2 = "checked" if $midbanna;      
	$tmp3 = ""; $tmp3 = "checked" if $botbanna;      
print <<EOADMN;
    <td colspan="2" align="right" $msg_cellclr width="25%">$defont
    Enable Photos:<input type="checkbox" name="usepics" $tmp value="1"></FONT></td>
    <td $msg_cellclr align="right" colspan="2" width="25%">$defont
    Enable Top Banner:<input type="checkbox" name="ban1" $tmp1 value="1"></FONT></td>
    <td $msg_cellclr align="right" colspan="2" width="25%">$defont
    Enable Mid. Banner:<input type="checkbox" name="ban2" $tmp2 value="1"></FONT></td>
    <td $msg_cellclr align="right" colspan="2" width="25%">$defont
    Enable Bot. Banner:<input type="checkbox" name="ban3" $tmp3 value="1">&nbsp;</FONT></td>
  </tr><tr>
EOADMN
	$tmp = ""; $tmp = "checked" if $wbmstr_notify;      
	$tmp1 = ""; $tmp1 = "checked" if $thanks_mail;      
	$tmp2 = ""; $tmp2 = "checked" if $add_blank;      
print <<EOADMN;
    <td colspan="2" align="right" $msg_cellclr>$defont
    Notify Webmaster:<input type="checkbox" name="webnotif" $tmp value="1"></FONT></td>
    <td $msg_cellclr align="right" colspan="2" width="25%">$defont
    Thankyou E-Mail:<input type="checkbox" name="thnks" $tmp1 value="1"></FONT></td>
    <td $msg_cellclr align="right" colspan="2" width="25%">$defont
    &quot;_blank&quot; in URL:<input type="checkbox" name="blank" $tmp2 value="1"></FONT></td>
    <td $msg_cellclr align="center" colspan="2" width="25%">$defont
EOADMN
	if ($i_we eq "I") {print "    &quot;I&quot;<input type=\"radio\" name=\"iwe\" checked value=\"I\">\n    &quot;we&quot;<input type=\"radio\" name=\"iwe\" value=\"we\"> E-Mail</FONT></td>\n";}
	else {print "    &quot;I&quot;<input type=\"radio\" name=\"iwe\" value=\"I\">\n    &quot;we&quot;<input type=\"radio\" name=\"iwe\" checked value=\"we\"> E-Mail</FONT></td>\n";}
print <<EOADMN;
  </tr><tr>
    <td colspan="8" align="center" $msg_cellclr><hr></td>
  </tr><tr>
    <td colspan="2" align="right" $msg_cellclr>$defont Webmaster E-Mail: </FONT></td>
    <td colspan="6" align="left" $msg_cellclr><input type="text" name="webmail" size="35" value="$webmstr"></td>
  </tr><tr>
    <td colspan="2" align="right" $msg_cellclr>$defont Name of Site: </FONT></td>
    <td colspan="6" align="left" $msg_cellclr><input type="text" name="site_is" size="35" value="$siteis"></td>
  </tr><tr>
    <td colspan="2" align="right" $msg_cellclr>$defont Name of List: </FONT></td>
    <td colspan="6" align="left" $msg_cellclr><input type="text" name="list_is" size="25" value="$listis"></td>
  </tr><tr>
    <td colspan="8" align="center" bgcolor="#CCCCCC">$defont
    <font color="#000000">Admin Password:</font></FONT><input type="password" name="admnpwd" size="12">&nbsp;&nbsp;
    <input type="submit" value="Submit Default Changes" name="B1"> &nbsp;&nbsp;<input 
    type="reset" value="Reset" name="B2"></td>
  </tr>
</table></center>
</form>
<center>$defont<BIG><strong><a href="$htm_url">The Book</a> &#149; <a href="$vizAdminScrpt?frmrecs=y">Records and Photos</a> &#149;</strong></BIG></FONT>
<P><font size="-1">VizBook v1.56, copyright 1999 - dtp-aus.com</center>
</body></html>
EOADMN
}
sub set_defaults {
	open(RC,"<$cnfg_url") || &showErr('Config-File Read Access');
	 eval" flock(RC,2)";
		@confg = <RC>;
	 eval" flock(RC,8)";
	close(RC);
for ($s1 = 0; $s1 < @confg; $s1++) {
if ($confg[$s1] =~ /\$bk_bgimg/) {
	if ($FORM{lstbgimg} && $FORM{lstbgimg} !~ /(.jpg|.gif)$/i) {showErr('List Background not .jpg/.gif');}
	$confg[$s1] = "\$bk_bgimg = \"$FORM{lstbgimg}\";\n";
}
if ($confg[$s1] =~ /\$add_bgimg/) {
	if ($FORM{addbgimg} && $FORM{addbgimg} !~ /(.jpg|.gif)$/i) {showErr('AddForm Background not .jpg/.gif');}
	$confg[$s1] = "\$add_bgimg = \"$FORM{addbgimg}\";\n";
} 
if ($confg[$s1] =~ /\$per_page/) {
	if (!$FORM{perpge} || $FORM{perpge} !~ /^[0-9]+$/) {$FORM{perpge} = 35;}
	$confg[$s1] = "\$per_page = \"$FORM{perpge}\";\n";
}
if ($confg[$s1] =~ /\$tbl_wid/) {$confg[$s1] = "\$tbl_wid = \"$FORM{tblwid}\";\n";}
if ($confg[$s1] =~ /\$shw_url/) {$confg[$s1] = "\$shw_url = \"$FORM{shwurl}\";\n";}
if ($confg[$s1] =~ /\$shw_cmpny/) {$confg[$s1] = "\$shw_cmpny = \"$FORM{shwcomp}\";\n";}
if ($confg[$s1] =~ /\$shw_city/) {$confg[$s1] = "\$shw_city = \"$FORM{shwcty}\";\n";}
if ($confg[$s1] =~ /\$list_email/) {$confg[$s1] = "\$list_email = \"$FORM{lstmail}\";\n";}
if ($confg[$s1] =~ /\$shw_icq/) {$confg[$s1] = "\$shw_icq = \"$FORM{shwicq}\";\n";}
if ($confg[$s1] =~ /\$list_miscbox/) {$confg[$s1] = "\$list_miscbox = \"$FORM{lstmisc}\";\n";}
if ($confg[$s1] =~ /\$list_drpdwn/) {$confg[$s1] = "\$list_drpdwn = \"$FORM{lstmnu}\";\n";}
if ($confg[$s1] =~ /\$pref_fnt/) {$confg[$s1] = "\$pref_fnt = \"$FORM{fname}\";\n";}
if ($confg[$s1] =~ /\$sze_3/) {$confg[$s1] = "\$sze_3 = \"$FORM{fsize}\";\n";}
if ($confg[$s1] =~ /\$use_divider/) {$confg[$s1] = "\$use_divider = \"$FORM{usediv}\";\n";}
if ($confg[$s1] =~ /\$divider/) {
	if ($FORM{divname} && $FORM{divname} !~ /(.jpg|.gif)$/i) {showErr('Divider not .jpg/.gif');}
	$confg[$s1] = "\$divider = \"$FORM{divname}\";\n"; $divider = $FORM{divname};
}
if ($confg[$s1] =~ /\$dvdr_wid/) {
	if ($FORM{divname} && $FORM{divwid} !~ /^[0-9]+$/) {showErr('Divider Width Error');}
	if ($tbl_wid eq 590 && $FORM{divwid} > 515) {$FORM{divwid} = 515;}
	$confg[$s1] = "\$dvdr_wid = \"$FORM{divwid}\";\n";
}
if ($confg[$s1] =~ /\$dvdr_hgt/) {
	if ($FORM{divname} && $FORM{divhgt} !~ /^[0-9]+$/) {showErr('Divider Height Error');}
	if ($FORM{divhgt} > 70) {$FORM{divhgt} = 70;}
	$confg[$s1] = "\$dvdr_hgt = \"$FORM{divhgt}\";\n";
}
if ($confg[$s1] =~ /\$bk_bgcolr/) {
	$FORM{bgclr} =~ s/(#| )//g;
	if ($FORM{bgclr}) {$FORM{bgclr} = "#$FORM{bgclr}";}
		$confg[$s1] = "\$bk_bgcolr = \"".&ucase($FORM{bgclr})."\";\n";
}
if ($confg[$s1] =~ /\$bk_text/) {
	$FORM{txtclr} =~ s/(#| )//g;
	if ($FORM{txtclr}) {$FORM{txtclr} = "#$FORM{txtclr}";}
	$confg[$s1] = "\$bk_text = \"".&ucase($FORM{txtclr})."\";\n";
}
if ($confg[$s1] =~ /\$bk_lnk/) {
	$FORM{lnkclr} =~ s/(#| )//g;
	if ($FORM{lnkclr}) {$FORM{lnkclr} = "#$FORM{lnkclr}";}
	$confg[$s1] = "\$bk_lnk = \"".&ucase($FORM{lnkclr})."\";\n";
}
if ($confg[$s1] =~ /\$bk_vlnk/) {
	$FORM{vlnkclr} =~ s/(#| )//g;
	if ($FORM{vlnkclr}) {$FORM{vlnkclr} = "#$FORM{vlnkclr}";}
	$confg[$s1] = "\$bk_vlnk = \"".&ucase($FORM{vlnkclr})."\";\n";
}
if ($confg[$s1] =~ /\$nme_cellclr/) {
	$FORM{namesclr} =~ s/(#| )//g;
	if ($FORM{namesclr}) {
		$FORM{namesclr} = "#$FORM{namesclr}";
		$FORM{namesclr} =~ s/(bgcolor|\")//g;
		$confg[$s1] = "\$nme_cellclr = \"bgcolor=\\\"".&ucase($FORM{namesclr})."\\\"\";\n";
	}
	else {$confg[$s1] = "\$nme_cellclr = \"\";\n";}
	}
if ($confg[$s1] =~ /\$msg_cellclr/) {
	$FORM{msgclr} =~ s/(#| )//g;
	if ($FORM{msgclr}) {
		$FORM{msgclr} = "#$FORM{msgclr}";
		$FORM{msgclr} =~ s/(bgcolor|\")//g;
		$confg[$s1] = "\$msg_cellclr = \"bgcolor=\\\"".&ucase($FORM{msgclr})."\\\"\";\n";
	}
	else {$confg[$s1] = "\$msg_cellclr = \"\";\n";}
	}
if ($confg[$s1] =~ /\$tb_tbleclr/) {
	$FORM{tblclr} =~ s/(#| )//g;
	if ($FORM{tblclr}) {
		$FORM{tblclr} = "#$FORM{tblclr}";
		$FORM{tblclr} =~ s/(bgcolor|\")//g;
		$confg[$s1] = "\$tb_tbleclr = \"bgcolor=\\\"".&ucase($FORM{tblclr})."\\\"\";\n";
	}
	else {$confg[$s1] = "\$tb_tbleclr = \"\";\n";}
	}
if ($confg[$s1] =~ /\$tb_cellclr/) {
	$FORM{celclr} =~ s/(#| )//g;
	if ($FORM{celclr}) {
		$FORM{celclr} = "#$FORM{celclr}";
		$FORM{celclr} =~ s/(bgcolor|\")//g;
		$confg[$s1] = "\$tb_cellclr = \"bgcolor=\\\"".&ucase($FORM{celclr})."\\\"\";\n";
	}
	else {$confg[$s1] = "\$tb_cellclr = \"\";\n";}
	}
if ($confg[$s1] =~ /\$misc_clr/) {
	$FORM{mscclr} =~ s/(#| )//g;
	if ($FORM{mscclr}) {$FORM{mscclr} = "#$FORM{mscclr}";}
	$confg[$s1] = "\$misc_clr = \"".&ucase($FORM{mscclr})."\";\n";
}
if ($confg[$s1] =~ /\$shw_miscbox/) {$confg[$s1] = "\$shw_miscbox = \"$FORM{usemisc}\";\n";}
if ($confg[$s1] =~ /\$miscbox_txt/) {
	if ($FORM{usemisc} && $FORM{misccapt} !~ /^\w+$/) {showErr('Misc. Box Caption Error');}
	$confg[$s1] = "\$miscbox_txt = \"$FORM{misccapt}\";\n";
}
if ($confg[$s1] =~ /\$miscbox_wid/) {
	if ($FORM{usemisc} && (!$FORM{mscwid} || $FORM{mscwid} !~ /^[0-9]+$/)) {$FORM{mscwid} = 25;}
	$confg[$s1] = "\$miscbox_wid = \"$FORM{mscwid}\";\n";
}
if ($confg[$s1] =~ /\$shw_drpdwn/) {$confg[$s1] = "\$shw_drpdwn = \"$FORM{usemnu}\";\n";}
if ($confg[$s1] =~ /\$drpdwn_txt/) {
	if ($FORM{usemnu} && $FORM{mnucapt} !~ /^\w+$/) {showErr('Menu Caption Error');}
	$confg[$s1] = "\$drpdwn_txt = \"$FORM{mnucapt}\";\n";
}
if ($confg[$s1] =~ /\$droptxt_wid/) {
	if ($FORM{usemnu} && (!$FORM{othrwid} || $FORM{othrwid} !~ /^[0-9]+$/)) {$FORM{othrwid} = 25;}
	$confg[$s1] = "\$droptxt_wid = \"$FORM{othrwid}\";\n";
}
if ($confg[$s1] =~ /\@dropdwn_items/ && ($FORM{aditem} || $FORM{mnuitms})) {
if ($FORM{mnuadd} eq "a") {
	$tmp = "@dropdwn_items";
	if ($tmp !~ /$FORM{aditem}/i) {
		push (@dropdwn_items,$FORM{aditem});
	foreach $s2 (@dropdwn_items) { $s3 .= "\'$s2\',"; }
	$confg[$s1] = "\@dropdwn_items = ($s3);\n";
}	}
elsif ($FORM{mnuadd} eq "d") {
	for($s2 = 0; $s2 < @dropdwn_items; $s2++) { 
	if ($dropdwn_items[$s2] =~ /$FORM{mnuitms}/i) {splice(@dropdwn_items,$s2,1); last;}
	}
	foreach $s2 (@dropdwn_items) { $s3 .= "\'$s2\',"; }
	$confg[$s1] = "\@dropdwn_items = ($s3);\n";
}
}
if ($confg[$s1] =~ /\$allow_pics/) {$confg[$s1] = "\$allow_pics = \"$FORM{usepics}\";\n";}
if ($confg[$s1] =~ /\$topbanna/) {$confg[$s1] = "\$topbanna = \"$FORM{ban1}\";\n";}
if ($confg[$s1] =~ /\$midbanna/) {$confg[$s1] = "\$midbanna = \"$FORM{ban2}\";\n";}
if ($confg[$s1] =~ /\$botbanna/) {$confg[$s1] = "\$botbanna = \"$FORM{ban3}\";\n";}
if ($confg[$s1] =~ /\$wbmstr_notify/) {$confg[$s1] = "\$wbmstr_notify = \"$FORM{webnotif}\";\n";}
if ($confg[$s1] =~ /\$thanks_mail/) {$confg[$s1] = "\$thanks_mail = \"$FORM{thnks}\";\n";}
if ($confg[$s1] =~ /\$add_blank/) {$confg[$s1] = "\$add_blank = \"$FORM{blank}\";\n";}
if ($confg[$s1] =~ /\$i_we/) {$confg[$s1] = "\$i_we = \"$FORM{iwe}\";\n";}
if ($confg[$s1] =~ /\$webmstr/) {
	if ($FORM{webnotif} && !&chk_addr($FORM{webmail})) {showErr('Webmasters E-Mail Address Error');}
	$s2 = $FORM{webmail};
	$s2 =~ s/(@.+$)//g;
	$confg[$s1] = "\$webmstr = \"$s2\\$1\";\n";
}
if ($confg[$s1] =~ /\$siteis/) {
	if ($FORM{site_is} !~ /^.+$/) {showErr('Site Name Error');}
	$confg[$s1] = "\$siteis = \"$FORM{site_is}\";\n";
}
if ($confg[$s1] =~ /\$listis/) {
	if ($FORM{list_is} !~ /^.+$/) {showErr('List Name Error');}
	$confg[$s1] = "\$listis = \"$FORM{list_is}\";\n";
}
}
	open(RC,">$cnfg_url") || &showErr('Config-File Write Access');
	 eval" flock(RC,2)";
		print RC @confg;
	 eval" flock(RC,8)";
	close(RC);
&noErr('Defaults Successfully Updated');
}
sub get_pics {
	opendir(DIR,"$admn_picspath/") || &showErr('Error Accessing Pics Directory'); 
		@files = sort(readdir(DIR));
	closedir(DIR);
	for($s1 = @files; $s1 >= 0; $s1--) {
		if ($files[$s1] !~ /^\d+(.gif|.jpg)/i) {
			push(@files2,$files[$s1]) if $files[$s1] =~ /(.gif|.jpg)/i && $files[$s1] !~ /^admn.*/i;
			splice(@files,$s1,1);
		}
	}
	@files2 = sort(@files2);
}
sub get_elists {
	$elists_is = "";
	if ( -e "$e_lists_cnfg") {
		open(EF,"<$e_lists_cnfg");
		 eval" flock(EF,2)";
			@elst = <EF>;
		 eval" flock(EF,8)";
		close(EF);

		foreach $s1 (@elst) {
			if ($s1 =~ /\$addr_only/ && $s1 =~ /(\".*\")/) {($addr_only = $1) =~ s/\"//g;}
			elsif ($s1 =~ /\$data_exten/ && $s1 =~ /(\".*\")/) {($data_exten = $1) =~ s/\"//g;}
			if ($data_exten) {$elists_is = " - <font color=\"#CC0000\">E-Lists Data found</font>";}
	}	}
}
sub ucase {
	local($s1) = @_;
	$s1 =~ tr/[a-z]/[A-Z}/;
 return $s1;
}
sub chk_addr {
    local($chk) = $_[0];
    if ($chk =~ /(.*@.*\.[a-zA-Z]{2,3}$)/ && $chk !~ /(^\.)|(\.$)|( )|(\.\.)|(@\.)|(\.@)|(@.*@)/) { return(1); }
    else { return(0); }
}
sub date_time {
	my($s1) = @_;
	my($mon,$year);
   ($mon,$year) = (gmtime($s1))[4,5];
	$mon++;
   	if ($year < 39) { $year = "20$year" }
   	elsif ($year > 99 && $year < 2000) { $year = 2000 + ( $year - 100 ) }
   	elsif ($year > 38) { $year = "19$year" }
   return ($mon,$year);
}
sub date_time_real {
   my($intime) = @_;
   my($min,$hour,$mday,$mon,$year);
   ($min,$hour,$mday,$mon,$year) = (gmtime($intime))[1,2,3,4,5];
	$mon++;
   	if ($year < 39) { $year = "20$year" }
   	elsif ($year > 99 && $year < 2000) { $year = 2000 + ( $year - 100 ) }
   	elsif ($year > 38) { $year = "19$year" }
	if ($dtUS eq "1") {local($datereal) = sprintf("%02d\/%02d\/%04d-%02d:%02d",$mon,$mday,$year,$hour,$min);}
	elsif ($dtUS eq "2") {local($datereal) = sprintf("%04d\/%02d\/%02d-%02d:%02d",$year,$mon,$mday,$hour,$min);}
	else {local($datereal) = sprintf("%02d\/%02d\/%04d-%02d:%02d",$mday,$mon,$year,$hour,$min);}
   return $datereal;
}
sub showErr {
	print "Content-type: text/html\n\n";
	print <<EOT;
	<html><head>
	<meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
	<title>Error Response</title></head>
	<body bgcolor="#FFFFFF" text="#000000" link="#000099">
	<center>&nbsp;<br><table width="420" border="0" cellspacing="0" cellpadding="1"><tr bgcolor="#FFFFFE">
      <td><font face="verdana, arial, geneva, helvetica" size="3"><b>'VizBook' Error Response</b></font></td></tr>
  </table><table cellpadding="1" cellspacing="0" border="0"><tr bgcolor="#FFFFFE"><td><font size="2" face="arial,helvetica,geneva">
	<p align="center"><b>The program has responded with an <font color="#FF0000">error</font></b></p></font>
        <dl><dt><font size="2" face="arial,helvetica,geneva">The result is:</font></dt><dd><font size="2" face="arial,helvetica,geneva"><font color="#CC0000"><b>$_[0]</b></font></font></dd>
        </dl><font size="2" face="arial,helvetica,geneva"><p align="center">Contact <a href="mailto:$webmstr?subject=Visitors Book Error">webmaster</a> if the problem persists</p></font></td>
    </tr><tr><td align=center bgcolor="#666666"><font size="2" face="arial,helvetica,geneva" color="#FFFFFF">Use your <b>Back Arrow</b> to return. <em>Thank you.</em></font></td>
    </tr><tr><td align=center bgcolor="#FFFFFE"><font face="arial, geneva, helvetica" size="1" color="#666666">VizBook v1.56, copyright 1999 - dtp-aus.com</font></td>
    </tr></table></center></body></html>
EOT
exit;
}
sub noErr {
	print "Content-type: text/html\n\n";
	print <<EOT;
	<html><head>
	<meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
	<title>Edit Complete</title></head>
	<body bgcolor="#FFFFFF" text="#000000" link="#0000FF" vlink="#0000FF">
	<center>&nbsp;<br><table width="420" border="0" cellspacing="0" cellpadding="1"><tr bgcolor="#FFFFFE">
      <td><b><font face="verdana, arial, geneva, helvetica" size="3">'VizBook' Edit Response</font></b></td>
    </tr></table><table border="0" cellspacing="0" cellpadding="1">
    <tr><td bgcolor="#FFFFFE"><font size="2" face="arial,helvetica,geneva"><p align="center"><b>The program reports <font color="#006600">success</font></b></p></font>
        <dl><dt><font size="2" face="arial,helvetica,geneva">Response:</font></dt>
          <dd><font size="2" face="arial,helvetica,geneva"> <font color="#004500"><b>$_[0]</b></font></font></dd></dl>
        <font size="2" face="arial,helvetica,geneva"><p align="center">Please click on a link below to refresh the Admin Page</font></td>
    </tr><tr><td align="center" bgcolor="#E5E5E5"><em><font size="2" face="arial, geneva, helvetica">Return to the</font></em> <font size="2" face="arial, geneva, helvetica"><a href="$vizAdminScrpt"><b>List Defaults</b></a> admin page.<br>
	<em>Return to the</em> <a href="$vizAdminScrpt?frmrecs=y"><b>Photos and Records</b></a> admin page.</font></td>
    </tr><tr><td align="center" bgcolor="#FFFFFE"><font size="1" color="#666666" face="arial, geneva, helvetica">VizBook v1.56, copyright 1999 - dtp-aus.com</font></td>
    </tr></table></center></body></html>
EOT
exit;
}
