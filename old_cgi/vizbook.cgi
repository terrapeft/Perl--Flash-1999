#! /usr/bin/perl

#   Welcome to the www.dtp-aus.com VizBook scripts. VERSION 1.56 Oct. 1999   #
# IMPORTANT INFORMATION THAT MUST BE READ IF YOU WISH TO USE THESE SCRIPTS   #
##############################################################################
# The scripts "VIZBOOK.CGI" and "VIZADMIN.CGI were written (and (c)) by Ron  #
# F Woolley, Melbourne Australia. Copyright 1999. These scripts CAN NOT BE   #
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
		$name =~ s/<([^>]|\n)*>//g; 
		$value =~ s/<([^>]|\n)*>//g unless $name eq "msg" && $allow_tgs == 1; 
		$value =~ s/<!--#(.|\n)*-->//g;
		$name =~ s/<!--#(.|\n)*-->//g;
		$value =~ s/<(.*href.*>|\/a)>//ig unless $name eq "msg" && $allow_tgs == 1;
		$value =~ s/(<.*?h\d.*?>|<.*?\/h.*?>)//mig;
		$value =~ s/\|/\//g;
		$name =~ s/\|/\//g;
		$value =~ s/`//g;
		$name =~ s/`//g;
		$value =~ s/\&/\&amp\;/g;
		$value =~ s/"/\&quot\;/g unless $allow_tgs == 1;
		$value =~ s/</\&lt\;/g unless $allow_tgs == 1;
		$value =~ s/>/\&gt\;/g unless $allow_tgs == 1;
	$FORM{$name} = $value;
	}
	&read_rjct_file;
	foreach $reject(@rjcts) {
		chomp($reject);
		if ($reject eq $ENV{'REMOTE_ADDR'}) {&showErr('Access Denied');}
		elsif (lc($reject) eq lc($FORM{'email'})) {&showErr('Access Denied');}   }
	if (!$FORM{'url'}) {$FORM{'url'} = "http://";}
	if (!$tbl_wid) {$tbl_wid = "590";} else {$tbl_wid = "95%";}
	if (!$sze_3) {$sze_3 = 2;}
	else {$sze_3 = 3;}
	$defont = "<FONT FACE=\"arial,geneva,helvetica\" SIZE=\"-1\">";
		if ($FORM{'adviz'}) {require $add_form; &do_type; &do_add_head; &add_entry;}
		elsif ($FORM{'nxtfrm'}) {&make_page;} 
		elsif ($FORM{'rstfrm'}) {&make_page;}
		elsif ($FORM{'addfrm'}) {require $add_form; &save_entry;} 
		else {&showErr('Unknown Response Requested');}
exit;
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
	 eval "flock(RF,2)";
		@vizrcrds = <RF>;
	 eval "flock(RF,8)";
	close(RF);
}
sub date_time {
local($s1) = @_;
if (!$s1) {$datein = time + $gmtPlusMinus;}
else {
	my($sec,$min,$hour,$mday,$mon,$year,$wday,$yday);
   ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = gmtime($s1);
   	if ($year < 39) { $year = "20$year" }
   	elsif ($year > 99 && $year < 2000) { $year = 2000 + ( $year - 100 ) }
   	elsif ($year > 38) { $year = "19$year" }
      local($apm = "am");
      local(@mnths) = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
      local(@days) = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
      if ($hour > 11) {$apm = "pm";}
      if ($hour > 12) {$hour =  $hour - 12;}
   $datein = sprintf("$days[$wday] $mday $mnths[$mon] %04d - %02d:%02d:<small>%02d$apm</small>",$year,$hour,$min,$sec);
}  }
sub do_type {
	print "Content-type: text/html\n\n";
print <<EOADD;
<html><head>
	<meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
	<title>Visitors Book (Submit Form)</title>
</head>
<body background="$admn_picsdir/$add_bgimg" bgcolor="#FFFFFF" text="000000" link="#0000CC" vlink="9900CC" alink="#FF0000">

EOADD
}
sub make_page {
	&read_rcrds; 
	if ($FORM{'nxtfrm'}) {$pics_dir = $admn_picsdir;}
	if ($FORM{'rstfrm'}) {$strt_num = @vizrcrds;} 
	$per_page = 35 if $per_page eq 0;
	$ttl_recs = @vizrcrds;
if ($add_blank) {$blnk = "\" target=\"_blank";}

	$cnts = $per_page; 
		if ($FORM{'nxtfrm'} && $FORM{'strt_is'}) {$strt_num = $FORM{'strt_is'};}
		elsif ($FORM{'addfrm'}) {$strt_num = $ttl_recs;}
	if ($strt_num < $per_page) {$cnts = $strt_num;}
  	$views .= "<font color=\"$misc_clr\">$cnts</font> of <font color=\"$misc_clr\">$ttl_recs</font> ";
		$s2 = 1;
		if ($FORM{'strt_is'}) {$views .= "| <strong>view page</strong> <a href=\"$htm_url\"><strong>$s2</strong></a>";}
		elsif ($ttl_recs > $per_page) {$views .= "| <strong>view page</strong> $s2";}
		$s2++;
		for($s1 = $ttl_recs - $per_page; $s1 > 0; $s1 = $s1 - $per_page) {
			if ($s1 ne $FORM{'strt_is'}) {$views .= " <a href=\"$vizbkScrpt?nxtfrm=y&strt_is=$s1\"><strong>$s2</strong></a>";}
			else {$views .= " $s2";}
		$s2++; }
	$do_midban = int($cnts / 2);

$page = <<EOTOP;
<html>

<head>
<title>$siteis (free to our guests)</title>
  <meta name="description" content="While at $siteis, place an entry in the Visitors Book - you will be a welcome guest. Feel free to come and browse around.">
  <meta name="keywords" content="visitor, guest, book, books, visitors, guests, free, image, images, bitmap, bitmaps, photo">
  <meta name="Author" content="user url = $htm_url : VizBook Script Copyright Ron F Woolley, 1998 - www.dtp-aus.com">

</head>

<body background="$pics_dir/0.jpg" bgcolor="$bk_bgcolr" text="$bk_text" link="$bk_lnk" vlink="$bk_vlnk" alink="#FF0000" bgproperties="fixed">
EOTOP
if ($topbanna) {require $banna1;}
	require $header;
if ($ttl_recs) {
  $page .= "<center><table border=\"0\" cellpadding=\"3\" cellspacing=\"0\" width=\"$tbl_wid\">\n";
  $page .= " <tr><td width=\"100%\" colspan=\"2\" align=\"center\"><font size=\"$sze_3\" face=\"$pref_fnt\">";
  $page .= $views;
  $page .= "</font></td></tr><tr><td width=\"100%\" colspan=\"2\"><hr noshade size=\"1\"></td></tr>\n";
	
    for($ss = $strt_num - 1; $cnts >= 1; $ss--) {
	($i1,$i2,$i3,$i4,$i5,$i6,$i7,$i8,$i9,$i10,$i11,$i12,$i13,$i14,$i17,$i18) = split(/\|/,$vizrcrds[$ss]);

    $page .= " <tr><td width=\"70\" align=\"right\" nowrap valign=\"top\"><font size=\"$sze_3\" face=\"$pref_fnt\">\n";
    $page .= "   <b>Name:<br>\n";
    if ($shw_cmpny && $i6) {$page .= "   Company:<br>\n";}
    if ($shw_city && $i11) {$page .= "   From:<br>\n";}
    if ($list_miscbox && $shw_miscbox && $i8) {$page .= "   $miscbox_txt:<br>\n";}
    if ($list_drpdwn && $shw_drpdwn && ($i9 || $i10)) {$page .= "   $drpdwn_txt:<br>\n";}
    $page .= "   Date:</b></font></td>\n";
    $page .= " <td valign=\"top\" align=\"left\" $nme_cellclr width=\"98%\"><font size=\"$sze_3\" face=\"$pref_fnt\">\n";
	$href = $i3;
    if ($shw_url && $i7) {$href = "<a href=\"$i7$blnk\">$i3</a>";}
    $page .= " $href";
if ($list_email) {
    $page .= " &nbsp;&nbsp;<b>Email:</b> <a HREF=\"mailto:$i4?subject=Your $listis entry.\">$i4</a>";
    if ($shw_icq && $i5) {$page .= "&nbsp;&nbsp;<b>ICQ#:</b> <a href=\"http://wwp.mirabilis.com/$i5$blnk\">$i5</a>";} 
}
    $page .= "<br>\n";
    if ($shw_cmpny && $i6) {$page .= "   $i6<br>\n";}
    if ($shw_city && $i11) {$page .= "   $i11, $i12 $i13<br>\n";}
    if ($list_miscbox && $shw_miscbox && $i8) {$page .= "   $i8<br>\n";}
    if ($list_drpdwn && $shw_drpdwn && ($i10 || $i9)) {
		if ($i10) {$page .= "   $i10<br>\n";}
		else {$page .= "   $i9<br>\n";}
    }
	if ($i17 =~ /^[0-9]+$/) {&date_time($i17);}
	else {$datein = $i17;}
    $page .= "   $datein</font></td>\n";
    $page .= " </tr><tr>\n";
    $page .= " <td width=\"70\" align=\"center\" valign=\"top\">\n";
    if ($allow_pics && $i14 && $i2 eq 1) {$page .= "  <img src=\"$pics_dir/$i14\" width=\"60\" height=\"60\" border=\"0\" align=\"middle\">";}
    $page .= " </td>\n";
    $page .= " <td valign=\"top\" align=\"left\" width=\"98%\" $msg_cellclr><font size=\"$sze_3\" face=\"$pref_fnt\">\&#149;\&nbsp;\&nbsp;\&nbsp;\n";
    $page .= "   $i18</font></td></tr>\n";
if ($cnts > 1) {
    $page .= " <tr><td width=\"70\"></td><td align=\"center\"";
	if ($use_divider) {$page .= " ><img src=\"$pics_dir/$divider\" align=\"middle\" width=\"$dvdr_wid\" height=\"$dvdr_hgt\" border=\"0\">";}
	else {$page .= " $nme_cellclr><hr width=\"100%\">";}
    $page .= "</td></tr>\n";
}
    $cnts--;
if ($do_midban eq $cnts && $midbanna && $do_midban > 1 ) {
    $page .= "</table></center>\n";
		require $banna2;
    $page .= "<center><table border=\"0\" cellpadding=\"3\" cellspacing=\"0\" width=\"$tbl_wid\">\n";
}
}
    $page .= " <tr><td width=\"100%\" colspan=\"2\"><hr noshade size=\"1\"></td></tr>\n";
    $page .= " <tr><td width=\"100%\" colspan=\"2\" align=\"center\"><font size=\"$sze_3\" face=\"$pref_fnt\">$views</font></td></tr>\n";
    $page .= "</table></center>\n";
}
else {$page .=   "<h2 align=\"center\">This page is new, and ready for your input!</h2>";}

if ($botbanna) {require $banna3;}
	require $footer;
    $page .= '<p align="center"><font size="1" face="arial,geneva,helvetica">VizBook v1.56, copyright 1999 - dtp-aus.com</small></small></p>'."\n";
    $page .= "</body></html>\n";

if (!$FORM{'nxtfrm'}) {
	open(HF,">$htm_path") || &showErr('HTML Page Read Access');
	 eval "flock(HF,2)";
		print HF $page;
	 eval "flock(HF,8)";
	close(HF);
				print "Location: $htm_url\n\n";
}
else {
				print "Content-type: text/html\n\n";
print $page; } 

}
sub resubmit_add {
local($adderror_is) = @_ ;
	&do_type;
		print "<h2 align=\"center\"><font color=\"#CC0000\">$adderror_is</font></h2>\n";
		$FORM{'msg'} =~ s/<br>/\n/ig;
		$FORM{'msg'} =~ s/<P>/\n\n/ig;
	&add_entry; 
}
sub read_rjct_file {
	if (-e,"<$rjctfile") {
		open(RF,"<$rjctfile") || &showErr('Reject File Read Access');
		eval "flock(RF,2)";
			@rjcts = <RF>;
		eval "flock(RF,8)";
		close(RF);    }
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
