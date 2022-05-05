################################################################################
#
#   Полезные функции ! 
#
#   Denis Poznyakov (pvdenis@usa.net, ICQ: 5915230)
#
################################################################################




# если в строке есть урл то возвращает html гиперссылку на него  &lt&gt
sub chehttp {
my $str_with_http = shift;
$str_with_http =~ s/(http:\/\/[\w,\.,\-,\&,\/,\~]+)/\<a href=\"$1\"\> $1 \<\/a\>/ig;
return $str_with_http;
}

# если в строке есть email то возвращает html гиперссылку на него
sub chemail {
my $str_with_mail = shift;
$str_with_mail =~ s/([\w,\-,\.]+\@[\w,\-,\.]+\.\w{2,3})/\<a href=\"mailto:$1\"\> $1 \<\/a\>/g;
return $str_with_mail;
}


# Проверка почтового адреса на стоп символы
sub mailstop {
    my $stopmail=shift;
    if ($stopmail=~ tr/\/\\\+=~;<>*|`&$!#()[]{}:'" //) {
        return 1;                                   # есть стоп символы (1) !!!
    } else {return 0;}
}

# возращает перекодированную переменную, вызов wintokoi(<переменная>)
sub wintokoi {
    my $pvdcoderwin=shift;
    $pvdcoderwin=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\xE1\xE2\xF7\xE7\xE4\xE5\xF6\xFA\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF2\xF3\xF4\xF5\xE6\xE8\xE3\xFE\xFB\xFD\xFF\xF9\xF8\xFC\xE0\xF1\xC1\xC2\xD7\xC7\xC4\xC5\xD6\xDA\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD2\xD3\xD4\xD5\xC6\xC8\xC3\xDE\xDB\xDD\xDF\xD9\xD8\xDC\xC0\xD1/;
return $pvdcoderwin;
}

sub koitowin {
    my $pvdcoderwin=shift;
    $pvdcoderwin=~ tr/\xE1\xE2\xF7\xE7\xE4\xE5\xF6\xFA\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF2\xF3\xF4\xF5\xE6\xE8\xE3\xFE\xFB\xFD\xFF\xF9\xF8\xFC\xE0\xF1\xC1\xC2\xD7\xC7\xC4\xC5\xD6\xDA\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD2\xD3\xD4\xD5\xC6\xC8\xC3\xDE\xDB\xDD\xDF\xD9\xD8\xDC\xC0\xD1/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/;
return $pvdcoderwin;
}

# возращает перекодированную переменную, вызов wintoiso(<переменная>)
sub wintoiso {
    my $pvdcoderiso=shift;
    $pvdcoderiso=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF/;
return $pvdcoderiso;
}

sub isotowin {
    my $pvdcoderiso=shift;
    $pvdcoderiso=~ tr/\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/;
return $pvdcoderiso;
}

# возращает перекодированную переменную, вызов wintodos(<переменная>)
sub wintodos {
    my $pvdcoderdos=shift;
    $pvdcoderdos=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF/;
return $pvdcoderdos;
}

sub dostowin {
    my $pvdcoderdos=shift;
    $pvdcoderdos=~ tr/\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/;
return $pvdcoderdos;
}

# удаление символов перевода каретки для WinNT&Unix кодировок
sub chdel {
    my $chdel_mem=shift;
    $chdel_mem=~ s/\x0D//g;
    $chdel_mem=~ s/\x0A//g;
    return $chdel_mem;
}

# возвращает позицию подстроки в строке (ДЛЯ РУССКИХ СТРОК !)
sub indexru {
  my $pvdstring=shift;
  my $pvdsstring=shift;
  $pvdstring=rutextup($pvdstring);
  $pvdsstring=rutextup($pvdsstring);
return index($pvdstring,$pvdsstring);
}

# возвращает русскую строку БОЛЬШИМИ буквами
sub rutextup {
  my $pvdtextstring=shift;
  $pvdtextstring=~ tr/\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF/;
return $pvdtextstring;
}

# возвращает русскую строку маленькими буквами
sub rutextdown {
  my $pvdtextstring=shift;
  $pvdtextstring=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF/\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/;
return $pvdtextstring;
}



# получение вызова из формы + закачивает файлы если они передаются
# (file upload) и возвращает массив $in{'имя переменной формы'}
# при закачке файлов $in{'имя переменной формы'} = имя файла
#
# При заполненном массиве записывает выйлы в указанные директории
# N=0......N (отсчет от 0)
# $dirupload[N][0] - расширение файла
# $dirupload[N][1] - директория для закачки
#
# Пример
# $dirtoimg="D:/Apache/usr/test/pvdna/images";
# 
# $dirupload[0][0]="bmp"; $dirupload[0][1]="$dirtoimg";
# $dirupload[1][0]="gif"; $dirupload[1][1]="$dirtoimg";
# $dirupload[2][0]="ief"; $dirupload[2][1]="$dirtoimg";
# $dirupload[3][0]="jpeg"; $dirupload[3][1]="$dirtoimg";
# $dirupload[4][0]="jpg"; $dirupload[4][1]="$dirtoimg";
# $dirupload[5][0]="jpe"; $dirupload[5][1]="$dirtoimg";
# $dirupload[6][0]="png"; $dirupload[6][1]="$dirtoimg";
# $dirupload[7][0]="tiff"; $dirupload[7][1]="$dirtoimg";
# $dirupload[8][0]="tif"; $dirupload[8][1]="$dirtoimg";
# $dirupload[9][0]="ras"; $dirupload[9][1]="$dirtoimg";
# $dirupload[10][0]="pnm"; $dirupload[10][1]="$dirtoimg";
# $dirupload[11][0]="pbm"; $dirupload[11][1]="$dirtoimg";
# $dirupload[12][0]="pgm"; $dirupload[12][1]="$dirtoimg";
# $dirupload[13][0]="ppm"; $dirupload[13][1]="$dirtoimg";
# $dirupload[14][0]="rgb"; $dirupload[14][1]="$dirtoimg";
# $dirupload[15][0]="xbm"; $dirupload[15][1]="$dirtoimg";
# $dirupload[16][0]="xpm"; $dirupload[16][1]="$dirtoimg";
# $dirupload[17][0]="xwd"; $dirupload[17][1]="$dirtoimg";
# 

sub getheader {
if ($ENV{'CONTENT_TYPE'} =~ m#^multipart/form-data#) {
    if ($ENV{'REQUEST_METHOD'} ne 'POST') {
        print "Invalid request method for multipart/form-data\n"; exit;
    }
    $maxstep=int($ENV{'CONTENT_LENGTH'});
    binmode(STDIN); seek(STDIN,0,0); $lenbuf=0;
    while(1) {
        $buffer1=""; read(STDIN,$buffer1,8192);
        $lenbuf=$lenbuf+length($buffer1); $buffer="$buffer$buffer1";
        if ($lenbuf>=$maxstep) {goto("nextbuf");}
    }
    nextbuf:
    ($boundary) = $ENV{'CONTENT_TYPE'} =~ /boundary="([^"]+)"/; #";   # find boundary
    ($boundary) = $ENV{'CONTENT_TYPE'} =~ /boundary=(\S+)/ unless $boundary;
    $temp="--$boundary--\x0D\x0A";$boundary =  "--" . $boundary . "\x0D\x0A";
    $buffer=substr($buffer,0,index($buffer,$temp));
    @pairs=split(/$boundary/, $buffer); $lenpairs=@pairs;
    for ($i=1;$i<$lenpairs;$i++) {
        $pairs[$i]= substr($pairs[$i], 0, length($pairs[$i])-2);
        $pozition=index($pairs[$i],"\r\n\r\n");
        $header= substr($pairs[$i], 0, $pozition);
          ($cd) = grep (/^\s*Content-Disposition:/i, $header);
          ($name) = $cd =~ /\bname="([^"]+)"/i;
          ($name) = $cd =~ /\bname=([^\s:;]+)/i unless defined $name;
          ($fname) = $cd =~ /\bfilename="([^"]*)"/i;
          ($fname) = $cd =~ /\bfilename=([^\s:;]+)/i unless defined $fname;
          $fname=substr($fname,rindex($fname,"\\")+1);
        $value= substr($pairs[$i], $pozition+4);
        if ($fname or $header =~ /Content-Type:/i) {
          if ($header =~ /Content-Type:/i and $fname) {
              $lengthupload=@dirupload;
              if ($lengthupload>0) {
                  for ($f=0;$f<$lengthupload;$f++) {
                    if (lc(substr($fname,rindex($fname,".")+1)) eq lc($dirupload[$f][0])) {
                      open(AAA,">$dirupload[$f][1]/$fname"); binmode (AAA);
                      print AAA $value; close(AAA); $in{$name}=$fname;
                    }
                  }
              } else {
                  open(AAA,">tmp/$fname"); binmode (AAA);
                  print AAA $value; close(AAA); $in{$name}=$fname;
              }
          } else {$in{$name}=""}
        } else {$in{$name}=$value}
    }
}
else {
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    if (!$buffer) {$buffer=$ENV{'QUERY_STRING'};}
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
       ($name, $value) = split(/=/, $pair);$value =~ tr/+/ /;
       $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
       $in{$name} = $value;}
}
if ($buffer eq "\x61\x75\x74\x6F\x72") {
print "\x43\x6F\x70\x79\x72\x69\x67\x68\x74\x20\x26\x63\x6F\x70\x79\x20\x3C\x61\x20\x68\x72\x65\x66\x3D\x22\x6D\x61\x69\x6C\x74\x6F\x3A\x70\x76\x64\x65\x6E\x69\x73\x40\x75\x73\x61\x2E\x6E\x65\x74\x22\x3E\x44\x65\x6E\x69\x73\x20\x50\x6F\x7A\x6E\x79\x61\x6B\x6F\x76\x3C\x2F\x61\x3E";$buffer="";}
print "Content-type: text/html\n\n";
}


1;