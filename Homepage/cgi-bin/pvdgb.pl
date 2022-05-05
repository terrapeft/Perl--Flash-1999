#! /usr/bin/perl

require "pvd-lib.pl";
require "pvdgb.cfg";


print "Content-type: text/html\n\n";

$date = `$date_command +"%A, %B %d, %Y at %T (%Z)"`; chop($date);
$shortdate = `$date_command +"%D %T %Z"`; chop($shortdate);
$datecommand = "/usr/bin/date/";
@months = ('01','02','03','04','05','06','07','08','09','10','11','12');
@days = ('Вс','Пн','Вт','Ср','Чт','Пт','Сб');
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time+($GMT*3600)))[0,1,2,3,4,5,6];
$year+=1900; $data = "  $days[$wday], $mday.$months[$mon].$year - $hour:$min";
#------------------------------------------------------------------------------
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

if ($buffer eq "") {
 $buffer=$ENV{'QUERY_STRING'};
}
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
   ($name, $value) = split(/=/, $pair);
   if ($name eq 'coder') {
      $coder=$value;
      $coder=~ s/%//g;
   }
    $value =~ tr/+/ /;
    $value =~ s/%7C/ /eg;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $value =~ s/\&/\&amp\;/g;
    $value =~ s/\"/\&quot\;/g;
    $value =~ s/</\&lt\;/g;
    $value =~ s/>/\&gt\;/g;
    $zapros{$name} = $value;
}
$no_enter_message=0; $url_get=$zapros{'url'}; $name_get=$zapros{'name'};
$e_mail_get=$zapros{'e_mail'}; $comentariy =$zapros{'coment'}; $coder=$zapros{'coder'};
$the_enter=$zapros{'w'}; &pustoy; print $end_h;
#------------------------------------------------------------------------------


sub pustoy {
if ($the_enter eq '1') {
#-------------------- Запись
    if (!$comentariy) {
        &no_comments;    # не введен коментарий 
    } else {
    if (!$name_get) {
        &no_name;        # не введено имя 
    }
    }
    &no_ban;

    if ($no_enter_message==0) {&no_error}

    # запрет
    if ($no_enter_message==0) {
    if ($url_get eq "http://") {$url_get=""}
    else {
        $url_get=~ tr/|/ /;
        $url_get=~ s/ //g;
    }
    $name_get=~ tr/|/ /;
    $e_mail_get=~ tr/|/ /;
    $e_mail_get=~ s/ //g;
    $comentariy =~ tr/|/ /;
    $comentariy=chehttp($comentariy);
    $comentariy=chemail($comentariy);
    $send_me_mail=wintokoi($comentariy);
    #-----------------------------------Проверка кодировки
   if ($coder eq 'koi8-r' and $how_to_keep==2) {
        $name_get=koitowin($name_get);
        $e_mail_get=koitowin($e_mail_get);
        $url_get=koitowin($url_get);
        $comentariy=koitowin($comentariy);
    }
    elsif ($coder eq 'koi8-r' and $how_to_keep==1) {
    }
   elsif ($coder eq 'iso-8859-5' and $how_to_keep==2) {
        $name_get=isotowin($name_get);
        $e_mail_get=isotowin($e_mail_get);
        $url_get=isotowin($url_get);
        $comentariy=isotowin($comentariy);
    }
    elsif ($coder eq 'iso-8859-5' and $how_to_keep==1) {
        $name_get=wintokoi(isotowin($name_get));
        $e_mail_get=wintokoi(isotowin($e_mail_get));
        $url_get=wintokoi(isotowin($url_get));
        $comentariy=wintokoi(isotowin($comentariy));
    }
   elsif ($coder eq 'cp866' and $how_to_keep==2) {
        $name_get=dostowin($name_get);
        $e_mail_get=dostowin($e_mail_get);
        $url_get=dostowin($url_get);
        $comentariy=dostowin($comentariy);
    }
    elsif ($coder eq 'cp866' and $how_to_keep==1) {
        $name_get=wintokoi(dostowin($name_get));
        $e_mail_get=wintokoi(dostowin($e_mail_get));
        $url_get=wintokoi(dostowin($url_get));
        $comentariy=wintokoi(dostowin($comentariy));
    }
    elsif ($coder eq 'windows-1251' and $how_to_keep==1) {
        $name_get=wintokoi($name_get);
        $e_mail_get=wintokoi($e_mail_get);
        $url_get=wintokoi($url_get);
        $comentariy=wintokoi($comentariy);
    }
    $comentariy=~ s/\x0D\x0A/\x01/g;
    #-----------------------------------
    open(FILE,">>$gb_db");
    print FILE "\n",$name_get,"|",$e_mail_get,"|",$url_get,"|",$data,"|",$comentariy,"|",$r_a,"|";
    close(FILE);
#-------------------------e_mail
    $mailprog = '/usr/sbin/sendmail';
    $snmail="killerjohn\@mail.spbnit.ru";
    open (MAIL, "|$mailprog -t");
    print MAIL "To: $snmail\n";
    print MAIL "From: My site\n";
    print MAIL "Subject: New Entry\n\n";
    print MAIL "$name_get\n$e_mail_get\n$url_get\n$send_me_mail";
    close(MAIL);
#-------------------------e_mail
    print $start_h;
    }
} else {print $start_h}
#-----------------------------------
print "\n<form name=puzogb method=get action=$resurs onSubmit=\"PreSubmit();\">\n",
    "<table width=$AllSh border=0 CELLPADDING=0 CELLSPACING=0>\n";
    if ($no_enter_message==0) {
        $inafprint=qq~<tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">Вас зовут:</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n<input type=text name=name size=40 class=border></td></tr><tr>
        <tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">e-mail:</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n<input type=text name=e_mail size=40 class=border></td></tr><tr>
        <tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">URL (если есть):</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n<input type=text name=url value=\"http://\" size=40 class=border></td></tr><tr>
        <tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">Cообщение:</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n</td></tr>
        </td></tr></table><textarea name=coment wrap cols=51 rows=4 class=border></textarea><br>\n
        ~;
        if ($how_to_keep==1) {print wintokoi($inafprint)}
        else {print $inafprint}
    } else {
        $inafprint=qq~<tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">Вас зовут:</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n<input type=text name=name value=\"$name_get\" size=40 class=border></td></tr><tr>
        <tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">e-mail:</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n<input type=text name=e_mail value=\"$e_mail_get\" size=40 class=border></td></tr><tr>
        <tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">URL (если есть):</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n<input type=text name=url value=\"$url_get\" size=40 class=border></td></tr><tr>
        <tr ALIGN=LEFT VALIGN=TOP><td><font size=\"-1\" face=\"Verdana, Aryal\">Cообщение:</font>\n</td>\n<td ALIGN=LEFT VALIGN=TOP>\n</td></tr>
        </td></tr></table><textarea name=coment wrap cols=49 rows=4 class=border>$comentariy</textarea><br>
        ~;
        if ($how_to_keep==1) {print wintokoi($inafprint)}
        else {print $inafprint}
    }
        $inafprint=qq~
        <input type=hidden NAME=coder value=\"windows-1251\">
        <input type=hidden name=w value=1>
        <input type=submit value='Сказать' $for_input>
        </form>~;
        if ($how_to_keep==1) {print wintokoi($inafprint)}
        else {print $inafprint}
        &coder_get;
        &zapisi;
}


#--------------------------
sub zapisi {
open (FILE,$gb_db);
@GB=<FILE>;
close(FILE);
$SIZE=@GB;
if ($SIZE>$max_zap) {
    open (FILE,">$gb_db");
    for ($i=$SIZE-50;$i<=$SIZE;$i++) {
        $_=$GB[$i];
        print FILE $_;
    }
    close(FILE);
    open (FILE,$gb_db);
    @GB=<FILE>;
    close(FILE);
    $SIZE=@GB;
}
$zap=0;
$go=0;
$vivod=0;
$norm=0;
print $e_form;
print "<a name=\"messages\">\n";
if (!$zapros{'x'}) {
    $zapros{'x'}=1;
    if ($SIZE>$max_messa) {
        $max_messa0=$max_messa+1;
        $back_next="<a href=\"$resurs?x=$max_messa0#messages\"><small><<</small></a> ";
        }

}
else {
   if ($zapros{'x'}<=$max_messa) {
       $nex=$max_messa+1;
       $next="$resurs?x=$nex#messages";
       $back="$resurs";
       $back_next="<a href=$next><small><<</small></a>\n<a href=$back><small>>></small></a>\n ";
   }
   else {
       $nex=$zapros{'x'}+$max_messa;
       $bac=$zapros{'x'}-$max_messa;
       if ($bac==1) {
        if ($nex>=$SIZE) {
               $back="$resurs";
               $back_next="<a href=$back><small>>></small></a>  ";
        }
        else {
           $next="$resurs?x=$nex#messages";
           $back="$resurs";
           $back_next="<a href=$next><small><<</small></a>\n<a href=$back><small>>></small></a>\n ";
        }
       }
       else {
        if ($nex>=$SIZE) {
           $back="$resurs?x=$bac#messages";
           $back_next="<a href=$back><small>>></small></a>  ";
        }
        else {
           $next="$resurs?x=$nex#messages";
           $back="$resurs?x=$bac#messages";
           $back_next="<a href=$next><small><<</small></a>\n<a href=$back><small>>></small></a>\n ";
        }
       }
   }
}
print "<table bgcolor=#eeeeee width=$AllSh border=0 CELLPADDING=0 CELLSPACING=0><tr><td>";
print $back_next;
if ($SIZE>$max_messa) {
    print "&nbsp;&nbsp;&nbsp;<small><small>[ ";
    for ($h=int($SIZE/$max_messa);$h>=1;$h--) {
        $page=$h*$max_messa+1;
        print " <a href=$resurs?x=$page#messages>",$h+1,"</a> ";
    }
    print " <a href=$resurs>1</a> ] ($SIZE)</small></small>";
}
   $float=0;
print "</td></tr></table><br>";

for ($i=$SIZE;$i>=0;$i--) {
  if ($GB[$i] ne "") {
   $zap=$zap+1;
  if ($zap==$zapros{'x'}) {
    $go=1;
  }
  else {
    if ($zap==$zapros{'x'}+$max_messa) {
        $go=0;
        $i=0;
        }
  }
   if ($go==1) {
    chomp($GB[$i]);
    @record=split(/\|/,$GB[$i]);
     $vivod=$vivod+1;
     $mas_gb[$vivod][0]=$record[0];  #Имя
     $mas_gb[$vivod][1]=$record[1];  #Е-МЫл
     $mas_gb[$vivod][2]=$record[2];  #УРЛ
     $mas_gb[$vivod][3]=$record[3];  #дата/время
     $mas_gb[$vivod][4]=$record[4];  #коментарий
   }
  }
}
for ($i=0;$i<=$vivod;$i++) {
$message0=$message;
$mainMName="";
$mainMUrl="";
$mainMMessage="";
if ($mas_gb[$i][0]) {
print $start_r;
   # Проверка на наличие почты
     if ($mas_gb[$i][1]) {
        $mainMName="<a href=\"mailto:$mas_gb[$i][1]\">$mas_gb[$i][0]</a>\n",
          " ";
     } else {
        $mainMName="$mas_gb[$i][0]\n";
     }
   # Проверка на URL
     if ($mas_gb[$i][2]) {
        $mainMUrl="<a href=\"$mas_gb[$i][2]\" target=\"newwind\">$urlMain</a>\n";
     } else {
        $mainMUrl="";
     }
     $mas_gb[$i][4]=~ s/\x01/ <br> /g;
     if (length($mas_gb[$i][4])>$max_buk) {
        @info_msg=split(/ /,$mas_gb[$i][4]);
        $size_msg=@info_msg;
        for ($i_msg=0;$i_msg<$size_msg;$i_msg++) {
          chomp($info_msg[$i_msg]);
          $info_go=$info_msg[$i_msg];

          if ($info_go) {
            if (length($info_go)>$max_buk and substr($info_go,0,5) ne "href=") {
                $to_prn="";
                for ($hj=0;$hj<=int(length($info_go)/$max_buk)-1;$hj++) {
                    $to_p=substr($info_go,$hj*$max_buk,$max_buk);
                    $to_prn="$to_prn$to_p <br>\n";
                }
                $hj=($hj)*$max_buk;
                $to_p=substr($info_go,$hj,length($info_go)-$hj);
                $to_prn="$to_prn$to_p\n";
                $mainMMessage="$mainMMessage $to_prn";
            }
            else {
                $mainMMessage="$mainMMessage $info_go";
            }
          }
        }
     }
     else {$mainMMessage="$mas_gb[$i][4]"}
     $message0=~ s/<name>/$mainMName/igm;
     $message0=~ s/<url>/$mainMUrl/igm;
     $message0=~ s/<mes>/$mainMMessage/igm;
     $message0=~ s/<date>/$mas_gb[$i][3]/igm;
     print $message0; print $end_r;
}
}
print "<table bgcolor=#eeeeee width=$AllSh border=0 CELLPADDING=0 CELLSPACING=0><tr><td>";
print $back_next;
if ($SIZE>$max_messa) {
    print "&nbsp;&nbsp;&nbsp;<small><small>[ ";
    for ($h=int($SIZE/$max_messa);$h>=1;$h--) {
        $page=$h*$max_messa+1;
        print " <a href=$resurs?x=$page#messages>",$h+1,"</a> ";
    }
    print " <a href=$resurs>1</a> ] ($SIZE)</small></small>";
}
print "</td></tr></table><br>";
}


sub no_name {
print $start_h;
print "<p type=table><font size=\"+1\" Color=red>Вы не ввели имя !<br><small>Запись не внесена.</small></font></p>";
$no_enter_message=1;
}

#--------------------------
sub no_comments {
print $start_h;
print "<p type=table><font size=\"+1\" Color=red>Вы не ввели сообщение !<br><small>Запись не внесена.</small></font></p>";
$no_enter_message=1;
}

#--------------------------
sub no_ban {
# Проверка на бан
    $r_a=$ENV{'REMOTE_ADDR'};
    open(BAN,"<$ban_ip_db");
    @GB_BAN=<BAN>;
    close(BAN);
    $SIZE_BAN=@GB_BAN;
        for ($not_go=0;$not_go<=$SIZE_BAN;$not_go++) {
        $_=$GB_BAN[$not_go];
         if (/$r_a/) {
            print $start_h;
            print "<p type=table><font size=\"+1\" Color=red>Вам запрещено вносить сообщения !</font></p>";
            $no_enter_message=1;
            $not_go=$SIZE_BAN+1;
         }
        }
}

#--------------------------
sub no_error {
if (length($url_get)>$maxURL or length($name_get)>$maxNAME or length($e_mail_get)>$maxEMAIL or length($comentariy)>$maxCOMMENT) {
print $start_h;
    print "<p type=table><font size=\"+1\" Color=red>Длина записи превысила предел !</font></p>";
    $no_enter_message=1;
}
}

#--------------------------
sub coder_get {
print <<SCRIPT_
<script LANGUAGE=\"JavaScript\">
    ua=navigator.userAgent;
    v=navigator.appVersion.substring(0,1);
    ch=document.charset;
    if ((ua.lastIndexOf(\"MSIE\")!=-1) && (v!='1') && (v!='2') && (v!='3')) {
      if ((ch!=\"windows-1251\") && (ch!=\"koi8-r\") && (ch!=\"cp866\") && (ch!=\"iso-8859-5\"))
    document.puzogb.coder.value=\"windows-1251\";
      else
    document.puzogb.coder.value=document.charset;
        }
    else {
    if (ua.indexOf(\"Win\") != -1)
       document.puzogb.coder.value=\"windows-1251\";
    else if (ua.indexOf(\"DOS\") != -1 || ua.indexOf(\"OS/2\") != -1)
       document.puzogb.coder.value=\"cp866\";
    else if (ua.indexOf(\"Mac\") != -1)
        document.puzogb.coder.value=\"koi8-r\";
        else
        document.puzogb.coder.value=\"windows-1251\";
        }
</script>

<script language=\"JavaScript\">
    // sysadmin, set the host to the current PLEASE
    var sHost = \"$sHost\";
    function getCookieVal (offset)
    {
        var endstr = document.cookie.indexOf (\";\", offset);
        if (endstr == -1)
            endstr = document.cookie.length;
        return unescape(document.cookie.substring(offset, endstr));
    }
    function GetCookie (name)
    {
        var arg = name + \"=\";
        var alen = arg.length;
        var clen = document.cookie.length;
        var i = 0;
        while (i < clen)
        {
            var j = i + alen;
            if (document.cookie.substring(i, j) == arg)
                return getCookieVal (j);
            i = document.cookie.indexOf(\" \", i) + 1;
            if (i == 0) break;
        }
        return null;
    }
    function SetCookie (name, value, expires, path, domain, secure)
    {
        document.cookie = name + \"=\" + escape (value) +
            ((expires) ? \"; expires=\" + expires.toGMTString() : \"\") +
            ((path) ? \"; path=\" + path : \"\") +
            ((domain) ? \"; domain=\" + domain : \"\") +
            ((secure) ? \"; secure\" : \"\");
    }
    function DeleteCookie (name,path,domain)
    {
        if (GetCookie(name))
        {
            document.cookie = name + \"=\" +
                ((path) ? \"; path=\" + path : \"\") +
                ((domain) ? \"; domain=\" + domain : \"\") +
                \"; expires=Thu, 01-Jan-70 00:00:01 GMT\";
        }
    }
    function PreSubmit()
    {
        var expdate = new Date ();
        expdate.setTime (expdate.getTime() + (360 * 24 * 60 * 60 * 1000)); // 360 day from now
        SetCookie (\"puzogb_name\", document.puzogb.name.value, expdate, null, sHost);
        SetCookie (\"puzogb_e_mail\", document.puzogb.e_mail.value, expdate, null, sHost);
        SetCookie (\"puzogb_url\", document.puzogb.url.value, expdate, null, sHost);
    }
    function PreLoad()
    {
        var sTemp = GetCookie (\"puzogb_name\");
        if (sTemp != null) document.puzogb.name.value = sTemp;
        sTemp = GetCookie (\"puzogb_e_mail\");
        if (sTemp != null) document.puzogb.e_mail.value = sTemp;
        sTemp = GetCookie (\"puzogb_url\");
        if (sTemp != null) document.puzogb.url.value = sTemp;
    }
    PreLoad();
</script>

SCRIPT_
}
