#! /usr/bin/perl 
##############################################################################
# c2ezcount                        Version 1.0                               #
# Copyright 1998 Chad Casselman    c2@websitereporter.com                    #
# Created 05/07/98                 Last Modified 05/07/98                    #
# URL: http:/www.websitereporter.com                                         #
##############################################################################
##############################################################################
# COPYRIGHT NOTICE                                                           #
# Copyright 1998 Chad Casselman.    All Rights Reserved.                     #
#                                                                            #
# Counter may be used and modified free of charge by anyone so long as       #
# this copyright notice and the comments above remain intact.  By using this #
# code you agree to indemnify Chad Casselman from any liability that         #  
# might arise from it's use.                                                 #  
#                                                                            #
# Selling the code for this program without prior written consent is         #
# expressly forbidden.  In other words, please ask first before you try and  #
# make money off of my program.                                              #
#                                                                            #
# Obtain permission before redistributing this software over the Internet or #
# in any other medium.	In all cases copyright and header must remain intact.#
#                                                                            #
##############################################################################

#######################################################################
#########################> USER OPTIONS <##############################
#######################################################################
# NOTE:
# Please set the first line of this file "#!/usr/bin/perl" to the location
#  of perl on your server.  If you don't know ask your system admin.
#
# To call the counter just insert the following code in your page after 
# changing the "/location/to/script/" to the correct location.
#  <!--#exec cgi="/location/to/script/c2ezcount.cgi"-->

$countfile = "/home/kotenka1359/public_html/cgi-bin/c2ezcount.dat";
  # Location to the file to hold the current count.  Must be named c2ezcount.dat.
  # Just change the path to the file.

$invisible = "0";
  # "1": Counter will be invisible.
  # "0": Counter will be visible.

$block_repeats = "0";
  # "1": Blocks the reload button.
  # "0": Does not block the reload button.

$private = "0";
  # "1": Call must come from the site listed in @referers.
  # "0": Call can be from ANY site ANYWHERE!

@referers = ("websitereporter.com","www.websitereporter.com","209.130.97.145");
  # If private is "1" then set else leave at "0".
  # Must have www.domain.com, domain.com, and IP Address.
  # For more information see http://www.websitereporter.com/support

$digit_dir = "http://gris-souris.virtualave.net/images/digits";
  # URL of the digits. Must be accessable via web browser.

$ending ="gif";
  # Ending of digits, either "gif" or "jpg";

$same_digit_size = "1";
  # "1": If the digits are SAME sizes.      FASTER DISPLAY TIME
  # "0": If the digits are DIFFERENT sizes. SLOWER DISPLAY TIME
  
$width = "14";
  # Width of digits if the same size.

$height = "17";
  # Height of digits if the same size.
#______________________________________________________________________
# If you still need help see http://www.websitereporter.com/support
#  or please email mailto:c2ezcount@websitereporter.com
#######################################################################
########################> END USER OPTIONS <###########################
#######################################################################
###        !!!! DO NOT CHANGE ANYTHING BELOW THIS LINE !!!!         ###
#######################################################################

$host = $ENV{'REMOTE_HOST'}; 

if($private == 1) {
  &check_referer;
 }
&incrementcounter;
&check_invisibility;
$num = $length = length($count);
while ($num > 0) {
   $NUMS{$num} = chop($count);
   $num--;
}
$i = 1;
print "Content-type: text/html\n\n";
while ($i <= $length) {
   if($same_digit_size == "1"){
     print"<img src=\"$digit_dir/$NUMS{$i}\.gif\" width=$width height=$height\">";
   }else{
         print"<img src=\"$digit_dir/$NUMS{$i}\.$ending\">";
         }
   $i++;
 }
exit(0);


#######################################################################
# Checks for valid counter call
#
sub check_referer {
   if (@referers && $ENV{'HTTP_REFERER'}) {
      foreach $referer (@referers) {
         if ($ENV{'HTTP_REFERER'} =~ m/$referer/) {
            $ref = 1;
            last;
         }
      }
   }
   else {
      $ref = 1;
   }
   if ($ref != 1) {
      $badreferer = "$digit_dir/bad_referer.gif";
      print "Location: $badreferer\n\n";
      exit;
   }
}
#
#
#######################################################################

#######################################################################
# Checks for invisible counter
#
sub check_invisibility {
   if ($invisible == "1") {
      print "Content-type: text/html\n\n";
      print "\n";
	  exit(0);
   }
}
#
#
#######################################################################

#######################################################################
# Increment the counter file
#
sub incrementcounter {
  	if (-e $countfile) {open(COUNT,"+<$countfile") || die("Can't open $countfile: $!\n");
		flock(COUNT,$lock);
		$count = <COUNT>; 
     		chop $count;
            $lastvisitor = <COUNT>;
            chop $lastvisitor;
            if ( ($block_repeats == "1") && ($host == $lastvisitor) ) {
     	         $dont_log = "1";
             } else { $count++; }
 		$number = $count;
  	} else {open(COUNT,">$countfile") || die("Can't open $countfile: $!\n");
		flock(COUNT,$lock); 
		$count = 1;
  	}

  	seek(COUNT,0,0);
  	print (COUNT "$count\n$host\n");
  	flock(COUNT,$unlock);  
  	close(COUNT);
}
#
#
#######################################################################	
