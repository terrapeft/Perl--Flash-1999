#### British ("") or US ("1") or Internat ("2") date pattern ------#
$dtUS = "";

#### An array of accepted referers domain names / IP#s ------------#
@referers = ('gris-souris.virtualave.net','gris-souris.virtualave.net/cgi-bin/','right-now.virtualave.net');

#### Path to Mail, Records,Requires,Images, SEE readme ------------#
$mailprog = '/usr/sbin/sendmail';
$gmt_url = "sets/gmtset.pl";
$cnfg_url = "sets/vizbkset.pl";
$adminword_url = "vbook/vizbk.pw";
$add_form = "vbook/addform.r";
$add_heada = "vbook/addhead.r";
$edit_form = "vbook/editform.r";
$mailmsg = "vbook/mailmsg.r";
$header = "vbook/vizhead.r";
$footer = "vbook/vizfoot.r";
$edcom = "vbook/editcom.r";
$rjctfile = "vbook/rejects.r";
$allow_tgs = 1;
$mmax = 2500;
$banna1 = "vbook/ban1.r";
$banna2 = "vbook/ban2.r";
$banna3 = "vbook/ban3.r";
$htm_path = "../vizbook/vizbook.htm";
$pics_dir = "pics";
$admn_picspath = "../vizbook/pics";
$admn_picsdir = "../vizbook/pics";
$records_url = "vbook/rcrds.t";
$e_lists_cnfg = "sets/elistset.pl";
$elist_dir = "vbook/";

#### Visuals and layout options, SEE readme.txt file --------------#
$bk_bgimg = "";
$add_bgimg = "bg1.gif";
$divider = "gold.gif";
$dvdr_wid = "515";
$dvdr_hgt = "2";
$misc_clr = "#00FF";
$bk_bgcolr = "#0000FF";
$bk_text = "#000000";
$bk_lnk = "#FF0000";
$bk_vlnk = "#00FF";
### NOTE:---------------ie--"bgcolor=\"#CCFFFF\"";---
$tb_tbleclr = "bgcolor=\"#0000FF\"";
$tb_cellclr = "bgcolor=\"#322D9D\"";
$nme_cellclr = "";
$msg_cellclr = "";
#----------------------------------------------------

#### URL of the VIZBOOK.CGI script --------------------------------#
$vizbkScrpt = "http://gris-souris.virtualave.net/cgi-bin/vizbook.cgi";

#### URL of the VIZADMIN.CGI script -------------------------------#
$vizAdminScrpt = "http://gris-souris.virtualave.net/cgi-bin/vizadmin.cgi";

#### URL of the Visitors Book HTML page ---------------------------#
$htm_url = "http://gris-souris.virtualave.net/vizbook/vizbook.htm";

#### URL of preferred Home or Return page ---------------------------#
$return_url = "http://gris-souris.virtualave.net/titul/index.htm";

#### Name of Site (or page) ---------------------------------------#
$siteis = "Gris Souris Guestbook";

#### Name of List -------------------------------------------------#
$listis = "Ósouriséñêàÿ Guestbook";

#### Preferred Font Face. -----------------------------------------#
$pref_fnt = "arial,helvetica,twisted";

#### Preferred Font Size. "" = 2 (default),  "1" = 3 --------------#
$sze_3 = "1";

#### Table Width "" (default) = 590 pixels, "1" = 95% of window ---#
$tbl_wid = "0";

$shw_miscbox = "";
$miscbox_txt = "Club";
$miscbox_wid = "25";

$shw_drpdwn = "";
$drpdwn_txt = "Via";
$droptxt_wid = "25";
@dropdwn_items = ('','search engine','linked list','news group',);

$per_page = "20";
$allow_pics = "1";
$shw_cmpny = "1";
$shw_url = "1";
$shw_city = "1";
$shw_icq = "1";
$list_email = "1";
$list_miscbox = "1";
$list_drpdwn = "";

$use_divider = "1";
$add_blank = "";
$i_we = "I";

$thanks_mail = "1";
$wbmstr_notify = "1";
$webmstr = "gris\@mail.ru";

$topbanna = "";
$midbanna = "";
$botbanna = "";

#### List of words you do not want in the Viz Book. If you are offended by these words, then realise that they are a fact of life on the Internet and every effort should be made to remove them..
@low_lifes = ('shit','shat','shiton','shitface','shitfaced','shitted','piss','pissed','pissoff','fart','farted','damn','bastard','bastards','bugger','bugga','bloody','bludy','bluddy','fuck','fucked','fuckt','fucker','fucking','fucken','fuckn','fuckin','fuckemall','fuckall','cunt','cunts','arsehole','arseholes','aholes','nigger','niggers','bitch','bitchs','motherfucker','motherfucka','muthafucka',);

1;	# this line MUST remain in all 'require' files.
