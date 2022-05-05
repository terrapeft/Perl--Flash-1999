#! /usr/bin/perl

use CGI qw(param);
use Time::Local;

$countfile = param("out");
$invisible = param("inv");
$block_repeats = "0";
$private = "0";
@referers = ("websitereporter.com","www.websitereporter.com","209.130.97.145");
$digit_dir = "http://gris-souris.virtualave.net/images/digits2";
$ending ="gif";
$same_digit_size = "1";
$width = "17";
$height = "18";

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
        @vcmonths = ('Пьянварь','Фигвраль','Кошмарт','Сопрель','Сымай','Теплюнь','Жарюль','Авгрусть','Свистябрь','Моктябрь','Гноябрь','Дубабрь');
        @vcdays = ('Вс','Пн','Вт','Ср','Чт','Пт','Сб');
        ($vcmin, $vchours, $vcday, $vcmonth, $vcwday)=(gmtime)[1, 2, 3, 4, 6];

        if ($vchours > 21) {
        $vchours+=3; 
        $vchours=$vchours-24;
        } else {$vchours+=3};

        if (length($vcmin)==1) {$vcmin="0"."$vcmin"};
        $vctime=$vcmonths[$vcmonth]." ".$vcday."   ".$vcdays[$vcwday]."   ".$vchours.":".$vcmin;
  	print (COUNT "$count\n$host\n$vctime\n");
  	flock(COUNT,$unlock);  
  	close(COUNT);
}
#
#
#######################################################################	
