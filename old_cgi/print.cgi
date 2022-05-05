#! /usr/bin/perl

open(OB, "0obnovka.dat");
$i=0;
while (<OB>){
 $_=~s/#.*//;
 @upgr[$i]=$_;
 $i++
}

open (IN, "0zaved.dat");
$z1="<font color=\"#FF0000\">".<IN>."</font>";
$z2=<IN>;
$z3="Текущая";
$z4=<IN>;
close (IN);

open (IN, "0tale.dat");
$sz1="<font color=\"#FF0000\">".<IN>."</font>";
$sz2=<IN>;
$sz3="<a href=\"april/fairy_tale.htm\" style=\"text-decoration:none\"  target=\"_blank\">Ознакомиться</a>";
$sz4=<IN>;
close (IN);

open (IN, "c2ezcount.dat");
$t1="<font color=\"#FF0000\">".<IN>."</font>";
$t2=<IN>;
$t3="<a href=\"titul/index.htm\" style=\"text-decoration:none\"  target=\"_blank\">Ознакомиться</a>";
$t4=<IN>;

close (IN);

open (IN, "0main.dat");
$ma1="<font color=\"#FF0000\">".<IN>."</font>";
$ma2=<IN>;
$ma3="<a href=\"main/index.htm\" style=\"text-decoration:none\"  target=\"_blank\">Ознакомиться</a>";
$ma4=<IN>;
close (IN);

open (IN, "0friends.dat");
$fr1="<font color=\"#FF0000\">".<IN>."</font>";
$fr2=<IN>;
$fr3="<a href=\"friends/index.htm\" style=\"text-decoration:none\"  target=\"_blank\">Ознакомиться</a>";
$fr4=<IN>;
close (IN);

open (IN, "0gallery.dat");
$gl1="<font color=\"#FF0000\">".<IN>."</font>";
$gl2=<IN>;
$gl3="<a href=\"gallery/index.htm\"  style=\"text-decoration:none\" target=\"_blank\">Ознакомиться</a>";
$gl4=<IN>;
close (IN);

open (IN, "0links.dat");
$l1="<font color=\"#FF0000\">".<IN>."</font>";
$l2=<IN>;
$l3="<a href=\"links/index.htm\"  style=\"text-decoration:none\" target=\"_blank\">Ознакомиться</a>";
$l4=<IN>;
close (IN);

open (IN, "0utils.dat");
$ut1="<font color=\"#FF0000\">".<IN>."</font>";
$ut2=<IN>;
$ut3="<a href=\"utility/index.htm\" style=\"text-decoration:none\"  target=\"_blank\">Ознакомиться</a>";
$ut4=<IN>;
close (IN);

open (IN, "0guest.dat");
$gt1="<font color=\"#FF0000\">".<IN>."</font>";
$gt2=<IN>;
$gt3="<a href=\"vizbook/vizbook.htm\" style=\"text-decoration:none\"  target=\"_blank\">Ознакомиться</a>";
$gt4=<IN>;
close (IN);



print <<STOP_IT;
Content-type: text/html

<table border="0" width="100%" bgcolor="#000000" cellspacing="1">
  <tr>
    <td style="font-family: Arial; font-size: 12pt; color: #00FF00; font-weight: bold" align="center" bgcolor="#800080" nowrap><font size="2" face="Arial">Страница</font></td>
    <td style="font-family: Arial; font-size: 12pt; color: #00FF00; font-weight: bold" align="center" bgcolor="#800080" nowrap><font size="2" face="Arial">Счетчик</font></td>
    <td style="font-family: Arial; font-size: 12pt; color: #00FF00; font-weight: bold" align="center" bgcolor="#800080" nowrap><font size="2" face="Arial">Время
      проникновения</font></td>
    <td style="font-family: Arial; font-size: 12pt; color: #00FF00; font-weight: bold" align="center" bgcolor="#800080" nowrap><font size="2" face="Arial">IP</font></td>
    <td style="font-family: Arial; font-size: 12pt; color: #00FF00; font-weight: bold" align="center" bgcolor="#800080" nowrap><font size="2" face="Arial">Последнее
      обновление</font></td>
    <td style="font-family: Arial; font-size: 12pt; color: #00FF00; font-weight: bold" align="center" bgcolor="#800080" nowrap><font size="2" face="Arial">Глянуть</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Daily
      Stats</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$z1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$z4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$z2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[0]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$z3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Сказка</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$sz1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$sz4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$sz2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">не
      подлежит</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$sz3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Индекс</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$t1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$t4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$t2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[1]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">Туда
      не нада</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Титул</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$t1</font>
    </td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$t4</font>
    </td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$t2</font>
    </td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[2]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$t3</font>
    </td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Я
      самая</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$ma1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$ma4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$ma2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[3]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$ma3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Галерея</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$gl1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$gl4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$gl2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[4]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$gl3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Друзья</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$fr1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$fr4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$fr2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[5]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$fr3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Гостевая</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$gt1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$gt4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$gt2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[6]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$gt3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Линки</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$l1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$l4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$l2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[7]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$l3</font></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="font-size: 12pt; font-family: Arial; color: #00FF00; font-weight: bold" nowrap><font color="#000000" size="2" face="Arial">Утилиты</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #00FFFF; font-weight: bold" align="center" nowrap><font color="#000000">$ut1</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$ut4</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$ut2</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$upgr[8]</font></td>
    <td bgcolor="#FFFFFF" style="font-family: Arial; font-size: 12pt; color: #FFFFFF" align="center" nowrap><font color="#000000">$ut3</font></td>
  </tr>
</table>



STOP_IT
