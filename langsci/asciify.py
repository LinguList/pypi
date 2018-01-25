# encoding=utf-8

FRENCH_REPLACEMENTS=[
  ('Œ','Oe'), 
  ('œ','oe')
  ]
GERMAN_REPLACEMENTS=[ 
  ('ß','ss') 
  ]
ICELANDIC_REPLACEMENTS=[
  ('Æ','Ae'),
  ('æ','ae'),
  ('Ð','d'),
  ('ð','d'),
  ('Þ','Th'),
  ('þ','th') 
  ]
  
asciiequivs = {'A':"ÀÁÂẦẤẪẨÃÃ̀Ã́Ã̂Ã̌Ã̍Ã̎ĀĀ̀Ā́Ā̂Ā̃Ā̃Ā̄Ā̆Ā̆Ā̈Ā̊Ā̌ĂẰẮẴẲȦȦ́ǠÄÄ́Ä̀Ä̂Ä̃ǞǞ̆Ä̆Ä̌ẢÅǺÅ̂Å̃Å̄Å̄Å̆A̋ǍA̍A̎ȀȂA̐A̓A̧À̧Á̧Â̧Ǎ̧A̭A̰À̰Á̰Ä̰Ä̰ĄĄ̀Ą́Ą̂Ą̃Ą̄Ą̄Ą̄Ą̄Ą̄Ą̇Ą̈Ą̈Ą̈Ą̈Ą̈Ą̈Ą̊Ą̌Ą̋Ą̱Ą̱Ą̱A᷎A̱À̱Á̱Â̱Ã̱Ā̱Ā̱Ā̱Ā̱Ä̱Ä̱Ä̱Ä̱Ä̱Å̱Ǎ̱A̱ẠẠ́Ạ̀ẬẠ̃Ạ̄ẶẠ̈Ạ̈Ạ̈Ạ̈Ạ̈Ạ̌Ạ̍A̤À̤Á̤Â̤Ä̤ḀḀ̂Ḁ̈A̯A̩A͔Ā͔ȺȺ̀Ⱥ́ᶏⱭ̀Ɑ́Ɑ̂Ɑ̃Ɑ̄Ɑ̆Ɑ̇Ɑ̈Ɑ̊Ɑ̌ᶐ",
'B':"B́B̂B̃B̄ḂB̈B̕ḆḆ̂ḄB̤B̥B̬ɃᵬᶀƁƂʙ̇ʙ̣",
'C':'C̀ĆĈC̃C̄C̄C̆ĊC̈ČČ́Č͑ČČ̕Č͑C̋C̓C̕C̔C͑ÇÇḈÇ̆Ç̇Ç̌C̦C̭C̱C̮C̣Ć̣Č̣C̥C̬C̯C̨ȻȻ̓ꞒƇɕꜾ',
'D':'D́D̂D̃D̄ḊD̊ĎD̑D̓D̕ḐD̦ḒḎD̮ḌḌ́D̤D̥D̬D̪ĐᵭᶁƉƊᶑƋȡꝹ́Ꝺ̇ᴅ̇ᴅ̣Ð́Ð̣',
'E':'ÈÉÊỀẾỄÊ̄Ê̌ỂẼẼ̀Ẽ́Ẽ̂Ẽ̌Ẽ̍Ẽ̎ĒḔḖĒ̂Ē̃Ē̃Ē̄Ē̆Ē̆Ē̌Ē̑ĔĔ̀Ĕ́Ĕ̄ĖĖ́Ė̃ËË̀Ë́Ë̂Ë̃Ë̄Ë̌ẺE̊E̊E̋ĚĚ́Ě̃Ě̋Ě̑E̍E̎ȄȆE̓E᷎ȨȨ̀Ȩ́Ȩ̂ḜȨ̌Ẽ̦ĘĘ̀Ę́Ę̂Ę̃Ę̃Ę̄Ę̄Ę̄Ę̄Ę̄Ę̄Ę̆Ę̇Ę̇Ę̈Ę̈Ę̈Ę̈Ę̈Ę̈Ę̋Ę̌Ę̑Ę̱Ę̱Ę̱Ę̣Ę᷎ȨḜḘḚE̱È̱É̱Ê̱Ẽ̱Ē̱Ḕ̱Ḗ̱Ē̱Ë̱Ë̱Ë̱Ë̱Ë̱Ě̱E̮Ē̮ẸẸ̀Ẹ́ỆẸ̃Ẹ̄Ẹ̄Ẹ̄Ẹ̄Ẹ̆Ẹ̆Ẹ̆Ẹ̈Ẹ̈Ẹ̈Ẹ̈Ẹ̈Ẹ̍Ẹ̌Ẹ̑E̤È̤É̤Ê̤Ë̤E̥E̯E̩È͕Ê͕Ẽ͕Ē͕Ḕ͕E̜E̹È̹É̹Ê̹Ẽ̹Ē̹Ḕ̹Ɇᶒⱸᶕᶓɚᶔɝ',
'F':'F̀F́F̄ḞF̓F̧ᵮᶂƑF̱F̣ꜰ̇Ꝼ́Ꝼ̇Ꝼ',
'G':'G̀ǴǴ̄ĜG̃G̃ḠḠ́ĞĠG̈G̈G̊G̋ǦǦ̈G̑G̒G̓G̕G̔ĢG̦G̱G̱G̮G̣G̤G̥G̫ꞠǤᶃƓɢ̇ɢ̣ʛƔ̓',
'H':'H̀H́ĤH̄ḢḦȞH̐H̓H̕ḨH̨H̭H̱ḪḤḤ̣H̤H̥H̬H̯ĦĦ̥ꞪⱧʜ̇Ꜧɧ',
'I':'ÌÍÎÎ́ĨĨ́Ĩ̀Ĩ̂Ĩ̌Ĩ̍ĪĪ́Ī̀Ī̂Ī̌Ī̃Ī̄Ī̆Ī̆ĬĬ̀Ĭ́İIİ́ÏÏ̀ḮÏ̂Ï̃Ï̄Ï̌Ï̑I̊I̋ǏỈȈȊI᷎ĮĮ̀Į́Į̂Į̃Į̄Į̄Į̄Į̄Į̄Į̄Į̈Į̈Į̈Į̈Į̈Į̈Į̋Į̌Į̱Į̱Į̱I̍I̐I̓I̧Í̧Ì̧Î̧I̭Ī̭ḬḬ́Ḭ̈Ḭ̈I̱Í̱Ì̱Î̱Ǐ̱Ĩ̱Ï̱Ḯ̱Ï̱Ï̱Ï̱Ī̱Ī̱Ī̱Ī̱I̮ỊỊ̀Ị́Ị̂Ị̃Ị̄Ị̈Ị̈Ị̈Ị̈Ị̈Ị̌Ị̍I̤Ì̤Í̤Î̤Ï̤I̥Í̥Ï̥I̯Í̯Ĩ̯I͔Ī͔ƗƗ̀Ɨ́Ɨ̂Ɨ̌Ɨ̃Ɨ̄Ɨ̈Ɨ̧Ɨ̧Ɨ̧Ɨ̧Ɨ̱Ɨ̱Ɨ̱Ɨ̱Ɨ̱Ɨ̱Ɨ̯ᶖ',
'J':'Ɩ̀Ɩ́Ɩ̃ᵼJ́ĴJ̃J̄J̇J̈J̈J̊J̋J̌J̌J̓J᷎J̱J̣J̣J̥ɈɈ̱ʝȷɟʄ',
'K':'K̀ḰK̂K̃K̄K̆K̇K̈ǨK̑K̓K̕K̔K͑ĶK̦K̨ḴḴ̓ḲK̮K̥K̬K̫ᶄƘⱩꝀꝂꝄꞢᴋ',
'L':'̇L̀ĹL̂L̃L̄L̇L̈L̋ĽL̐L̑L̓L̕ĻĻ̂Ļ̃L̦ḼḺḺ̓L̮ḶḶ̀Ḷ́ḸḸ́Ḹ̆Ḷ̓Ḷ̕Ḷ̣L̤L̤L̥L̥Ĺ̥L̥L̥L̥L̥L̩L̯ŁŁ̇Ł̓Ł̣Ł̱ꝈȽⱠⱢɬᶅɭꞎȴʟ̇ʟ̣ƛƛ̓λ̴λ̴',
'M':'̇M̀ḾM̂M̃M̄M̆ṀṀ̇M̈M̋M̍M̌M̐M̑M̓M̕M͑ᵯM̧M̨M̦M̱Ḿ̱M̮ṂṂ́Ṃ̄Ṃ̓M̥Ḿ̥M̥M̥M̥M̬M̩M̯ᶆⱮᴍ̇ᴍ̣',
'N':'ǸŃN̂ÑÑ̈N̄N̆ṄṄ̇N̈N̋ŇN̐N̑N̍N̓N̕ꞤᵰŅŅ̂Ņ̃N̦N̨ṊN̰ṈṈ́N̮ṆṆ́Ṇ̄Ṇ̄Ṇ̓N̤N̥Ǹ̥Ń̥Ñ̥Ñ̥N̥N̥N̥N̥Ṅ̥N̥N̥N̥N̯N̩N̲ƝȠꞐᶇɳȵɴ̇ɴ̣',
'O':'ÒÓÔỐỒỖỔÕÕ̍Õ̀ṌÕ̂Õ̌ṎȬŌṒṐŌ̂Ō̃Ō̃Ō̄Ō̆Ō̆Ō̈Ō̌ŎŎ̀Ŏ́Ŏ̈ȮȮ́ȰO͘Ó͘Ò͘Ō͘O̍ÖÖ́Ö̀Ö̂Ö̌Ö̃ȪȪ̆Ö̆ỎO̊ŐǑO̐ȌȎØØ̀ǾØ̂Ø̃Ø̄Ø̄Ø̄Ø̆Ø̇Ø̇Ø̈Ø̋Ø̌Ø᷎Ø̨Ǿ̨Ø̨Ø̣Ø̥Ø̰Ǿ̰ƟꝊƠỚỜỠỞO̍O̓O᷎Ó᷎O̧Ó̧Ò̧Ô̧Ǒ̧ǪǪ̀Ǫ́Ǫ̂Ǫ̃ǬǬ̀Ǭ́Ǭ̂Ǭ̃Ǭ̆Ǭ̌Ǫ̆Ǫ̆Ǫ̇Ǫ̇Ǫ̈Ǫ̈Ǫ̈Ǫ̈Ǫ̈Ǫ̈Ǫ̋Ǫ̌Ǫ̑Ǫ̣Ǫ̱Ǫ̱Ǫ̱Ǫ᷎O̭O̰Ó̰O̱Ò̱Ó̱Ô̱Ǒ̱Õ̱Ō̱Ṓ̱Ṑ̱Ō̱Ö̱Ö̱Ö̱Ö̱Ö̱O̮ỌỌ̀Ọ́ỘỌ̃Ọ̄Ọ̄Ọ̄Ọ̄Ọ̄Ọ̆Ọ̈Ọ̈Ọ̈Ọ̈Ọ̈Ọ̈Ọ̌Ọ̑ỢỌO̤Ò̤Ó̤Ô̤Ö̤O̥Ō̥O̬O̯Õ͔Ō͔O̜O̹Ó̹O̲ᴓᶗꝌⱺꝊƆ́Ɔ̀Ɔ̂Ɔ̌Ɔ̄Ɔ̃Ɔ̃Ɔ̃Ɔ̃Ɔ̃Ɔ̃Ɔ̄Ɔ̆Ɔ̈Ɔ̈Ɔ̈Ɔ̈Ɔ̈Ɔ̍Ɔ̇Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̣Ɔ̤Ɔ̤Ɔ̤Ɔ̤Ɔ̤Ɔ̱Ɔ̱Ɔ̱Ɔ̱Ɔ̱Ɔ̱Ɔ̱Ɔ̱Ɔ̱Ɔ̧Ɔ̧Ɔ̧Ɔ̧Ɔ̧Ɔ̨Ɔ̨Ɔ̨Ɔ̨Ɔ̨Ɔ̨Ɔ̨Ɔ̨Ɔ̱',
'P':'̇P̀ṔP̃P̄P̆ṖP̈P̋P̑P̓P̕P̔P͑P̱P̣P̤P̬ⱣꝐᵱᶈƤꝒꝔᴘ',
'Q':'̇Q́Q̃Q̄Q̇Q̈Q̋Q̓Q̕Q̧Q̣Q̣Q̣Q̱ꝖꝖ̃ꝘʠɊ',
'R':'R̀ŔR̂R̃R̄R̆ṘR̋ŘR̍ȐȒR̓R̕ŖR̦R̨R̨ꞦR̭ṞṚṚ̀Ṛ́ṜṜ́Ṝ̃Ṝ̆R̤R̥R̥Ŕ̥R̥R̥R̥R̥R̥Ř̥R̬R̩R̯ɌᵲɺᶉɻⱹɼⱤɾᵳɿʀ̇ʀ̣Ꝛ́Ꝛ',
'S':'̣S̀ŚŚ̀ŚṤŜS̃S̄S̆ṠṠ̃S̈S̋ŠŠ̀Š́ṦŠ̓S̑S̓S̕ŞȘS̨Š̨ꞨS̱Ś̱S̮ṢṢ́Ṣ̄ṨṢ̌Ṣ̕Ṣ̱S̤Š̤S̥Ś̥S̬S̪ꜱ̇ꜱ̣ſ́ẛſ̣ẞᶊʂⱾẜẝᶋᶘʆ',
'T':'T̀T́T̃T̄T̆T̆ṪT̈ŤT̑T̓T̕T̔T͑ŢȚT̨T̗ṰT̰ṮT̮ṬṬ́T̤T̥T̬T̯T̪ƾŦȾᵵƫƬƮȶᴛ̇ᴛ','U':'̣̇ÙÚÛŨŨ̀ṸŨ̂Ũ̊Ũ̌Ũ̍ŪŪ̀Ū́Ū̂Ū̌Ū̃Ū̄Ū̆Ū̆ṺŬŬ̀Ŭ́U̇U̇U̇ÜǛǗÜ̂Ü̃ǕǕ̆Ü̆ǙỦŮŮ́Ů̃ŰǓU̍ȔȖU̓U᷎ỦƯỨỪỮỬỰU̧Ú̧Ù̧Û̧Ǔ̧ŲŲ̀Ų́Ų̂Ų̌Ų̄Ų̄Ų̄Ų̄Ų̄Ų̄Ų̈Ų̈Ų̈Ų̈Ų̈Ų̈Ų̋Ų̱Ų̱Ų̱ṶṴṴ́Ṵ̈U̱Ù̱Ú̱Û̱Ũ̱Ū̱Ū̱Ū̱Ū̱Ü̱Ǘ̱Ǜ̱Ü̱Ǚ̱Ǔ̱ỤỤ̀Ụ́Ụ̂Ụ̃Ụ̄Ụ̈Ụ̈Ụ̈Ụ̈Ụ̈Ụ̌Ụ̍ṲṲ̀Ṳ́Ṳ̂Ṳ̈U̥Ü̥U̯Ũ̯Ü̯U͔Ũ͔Ū͔ɄɄ̀Ʉ́Ʉ̂Ʉ̃Ʉ̄Ʉ̈Ʉ̌Ʉ̧Ʉ̰Ʉ̰Ʉ̱Ʉ̱Ʉ̱Ʉ̱Ʉ̱Ʉ̱Ʉ̥ᵾᶙʮʯɰᵿ','V':'V̀V́V̂ṼṼ̀Ṽ́Ṽ̂Ṽ̌V̄V̄V̄V̄V̄V̄V̄V̄V̆V̆V̇V̈V̈V̈V̈V̈V̈V̊V̋V̌V̍V̏V̐V̓V̧V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̨V̱V̱V̱V̱V̱Ṽ̱V̱V̱V̱V̱V̱ṾV̥ꝞᶌƲⱱⱴꝨ́Ꝩ̇Ꝩ̣',
'W':'ẀẂŴW̃W̄W̆ẆẄW̊W̋W̌W̍W̓W̱ẈW̥W̬Ⱳ',
'X':'X̀X́X̂X̃X̄X̆X̆ẊẌX̊X̌X̓X̕X̱X̱X̣X̣X̥ᶍ',
'Y':'ỲÝŶỸȲȲ̀Ȳ́Ȳ̃Ȳ̆Y̆Y̆Y̆ẎẎ́ŸŸ́Y̊Y̋Y̌Y̍Y̐Y̓ỶY᷎Y̱ỴỴ̣Y̥Y̯ɎƳỾ',
'Z':'Z̀ŹẐZ̃Z̄ŻZ̈Z̋ŽŽ́Ž̏Z̑Z̓Z̕Z̨Z̗ẔZ̮ẒẒ́Ẓ̌Ẓ̣Z̤Z̥ƵᵶᶎȤʐʑⱿⱫƷ́Ʒ̇ǮǮ́Ʒ̥ᶚƺʓ',
'_':'Þ́Þ̣ꝤꝦƻꜮʡʢǀǁǃǂʘ',
#
'a':'àáâầấẫẩãã̀ã́ã̂ã̌ã̍ã̎āā̀ā́ā̂ā̃́ā̃́ā̄ā̆́ā̆́ā̈ā̊ā̌ăằắẵẳȧȧ́ǡää́ä̀ä̂ä̃ǟǟ̆ä̆ä̌ảåǻå̂å̃å̄̆å̄̆å̆a̋ǎa̍a̎ȁȃa̐a̓a̧à̧á̧â̧ǎ̧a̭a̰à̰á̰ä̰́ä̰́ąą̀ą́ą̂ą̃ą̄̀ą̄̀́ą̄́̂ą̄̂̌ą̄̌ą̇ą̈̀ą̈̀́ą̈́̂ą̈̂̌ą̈̌̄ą̈̄ą̊ą̌ą̋ą̱̀ą̱̀̀ą̱̀a᷎a̱à̱á̱â̱ã̱ā̱̀ā̱̀́ā̱́̂ā̱̂ä̱̀ä̱̀́ä̱́̂ä̱̂̌ä̱̌å̱ǎ̱̥a̱̥ạạ́ạ̀ậạ̃ạ̄ặạ̈̀ạ̈̀́ạ̈́̂ạ̈̂̌ạ̈̌ạ̌ạ̍a̤à̤á̤â̤ä̤ḁḁ̂ḁ̈a̯a̩a͔ā͔ⱥⱥ̀ⱥ́ɑ̀ɑ́ɑ̂ɑ̃ɑ̄ɑ̆ɑ̇ɑ̈ɑ̊ɑ̌',
'b':'b́b̂b̃b̄ḃb̈b̕ḇḇ̂ḅb̤b̥b̬ƀɓƃ',
'c':'c̀ćĉc̃c̄́c̄́c̆ċc̈čč́č͑č̓č̕č͑c̋c̓c̕c̔c͑çḉç̆ç̇ç̌c̦c̭c̱c̮c̣ć̣č̣c̥c̬c̯c̨ȼȼ̓ꞓƈꜿ',
'd':'d́d̂d̃d̄ḋd̊ďd̑d̓d̕ḑd̦ḓḏd̮ḍḍ́d̤d̥d̬d̪đɖɗƌꝺ́ꝺ̇ð́ð̣',
'e':'èéêềếễê̄ê̌ểẽẽ̀ẽ́ẽ̂ẽ̌ẽ̍ẽ̎ēḕḗē̂ē̃́ē̃́ē̄ē̆́ē̆́ē̌ē̑ĕĕ̀ĕ́ĕ̄ėė́ė̃ëë̀ë́ë̂ë̃ë̄ë̌ẻe̊̄e̊̄e̋ěě́ě̃ě̋ě̑e̍e̎ȅȇe̓e᷎ȩȩ̀ȩ́ȩ̂ḝȩ̌ẽ̦ęę̀ę́ę̂ę̃́ę̃́ę̄̀ę̄̀́ę̄́̂ę̄̂̃ę̄̃̌ę̄̌ę̆ę̇́ę̇́ę̈̀ę̈̀́ę̈́̂ę̈̂̌ę̈̌̄ę̈̄ę̋ę̌ę̑ę̱̀ę̱̀́ę̱́ę̣ę᷎ȩḝḙḛe̱è̱é̱ê̱ẽ̱ē̱ḕ̱ḗ̱̂ē̱̂ë̱̀ë̱̀́ë̱́̂ë̱̂̌ë̱̌ě̱e̮ē̮ẹẹ̀ẹ́ệẹ̃ẹ̄̀ẹ̄̀́ẹ̄́̃ẹ̄̃ẹ̆̀ẹ̆̀́ẹ̆́ẹ̈̀ẹ̈̀́ẹ̈́̂ẹ̈̂̌ẹ̈̌ẹ̍ẹ̌ẹ̑e̤è̤é̤ê̤ë̤e̥e̯e̩è͕ê͕ẽ͕ē͕ḕ͕e̜e̹è̹é̹ê̹ẽ̹ē̹ḕ̹ɇ',
'f':'f̀f́f̄ḟf̓f̧ƒf̱f̣ꝼ́ꝼ̇ꝼ̣',
'g':'g̀ǵǵ̄ĝg̃́g̃́ḡḡ́ğġg̈̇g̈̇g̊g̋ǧǧ̈g̑g̒g̓g̕g̔ģg̦g̱̓g̱̓g̮g̣g̤g̥g̫ꞡǥɠɣ̓',
'h':'h̀h́ĥh̄ḣḧȟh̐h̓h̕ḩh̨h̭ẖḫḥḥ̣h̤h̥h̬h̯ħħ̥ɦⱨꜧ',
'i':'ìíîî́ĩĩ́ĩ̀ĩ̂ĩ̌ĩ̍īī́ī̀ī̂ī̌ī̃ī̄ī̆́ī̆́ĭĭ̀ĭ́iıi̇́ïï̀ḯï̂ï̃ï̄ï̌ï̑i̊i̋ǐỉȉȋi᷎įį̀į́į̇́į̂į̃į̇̃į̄̀į̄̀́į̄́̂į̄̂̆į̄̆̌į̄̌į̈̀į̈̀́į̈́̂į̈̂̌į̈̌̄į̈̄į̋į̌į̱́į̱́̀į̱̀i̍i̐i̓i̧í̧ì̧î̧i̭ī̭ḭḭ́ḭ̈́ḭ̈́i̱í̱ì̱î̱ǐ̱ĩ̱ï̱ḯ̱̀ï̱̀̂ï̱̂̌ï̱̌ī̱́ī̱́̀ī̱̀̂ī̱̂i̮ịị̀ị́ị̂ị̃ị̄ị̈̀ị̈̀́ị̈́̂ị̈̂̌ị̈̌ị̌ị̍i̤ì̤í̤î̤ï̤i̥í̥ï̥i̯í̯ĩ̯i͔ī͔ɨɨ̀ɨ́ɨ̂ɨ̌ɨ̃ɨ̄ɨ̈ɨ̧̀ɨ̧̀̂ɨ̧̂̌ɨ̧̌ɨ̱̀ɨ̱̀́ɨ̱́̂ɨ̱̂̈ɨ̱̈̌ɨ̱̌ɨ̯ɩ̀ɩ́ɩ̃',
'j':'j́ĵj̃j̇̃j̄j̈̇j̈̇j̊j̋ǰ́ǰ́j̓j᷎j̱ǰ̣ǰ̣j̥ɉɉ',
'k':'̱k̀ḱk̂k̃k̄k̆k̇k̈ǩk̑k̓k̕k̔k͑ķk̦k̨ḵḵ̓ḳk̮k̥k̬k̫ƙⱪꝁꝃꝅꞣ',
'l':'l̀ĺl̂l̃l̄l̇l̈l̋ľl̐l̑l̓l̕ļļ̂ļ̃l̦ḽḻḻ̓l̮ḷḷ̀ḷ́ḹḹ́ḹ̆ḷ̓ḷ̕ḷ̣l̤̄l̤̄l̥̀l̥̀ĺ̥̄l̥̄̄́l̥̄́̄̆l̥̄̆̕l̥̕l̩l̯łł̇ł̓ł̣ł̱ꝉƚⱡɫ̓',
'm':'m̀ḿm̂m̃m̄m̆ṁṁ̇m̈m̋m̍m̌m̐m̑m̓̕m̕m͑m̧m̨m̦m̱ḿ̱m̮ṃṃ́ṃ̄ṃ̓m̥ḿ̥̄m̥̄̄́m̥̄́̄̆m̥̄̆m̬m̩m̯ɱ',
'n':'ǹńn̂ññ̈n̄n̆ṅṅ̇n̈n̋ňn̐n̑n̍n̓n̕ꞥņņ̂ņ̃n̦n̨ṋn̰ṉṉ́n̮ṇṇ́ṇ̄́ṇ̄́ṇ̓n̤n̥ǹ̥ń̥ñ̥́ñ̥́̄n̥̄̄́n̥̄́̄̆n̥̄̆̄̑n̥̄̑ṅ̥̑n̥̑̑́n̥̑́̑̄n̥̑̄n̯n̩n̲ɲƞꞑ',
'o':'òóôốồỗổõõ̍õ̀ṍõ̂õ̌ṏȭōṓṑō̂ō̃́ō̃́ō̄ō̆́ō̆́ō̈ō̌ŏŏ̀ŏ́ŏ̈ȯȯ́ȱo͘ó͘ò͘ō͘͘o̍͘öö́ö̀ö̂ö̌ö̃ȫȫ̆ö̆ỏo̊őǒo̐ȍȏøø̀ǿø̂ø̃ø̄́ø̄́̆ø̄̆ø̆ø̇́ø̇́ø̈ø̋ø̌ø᷎ø̨ǿ̨̄ø̨̄ø̣ø̥ø̰ǿ̰ɵꝋơớờỡởo̍o̓o᷎ó᷎o̧ó̧ò̧ô̧ǒ̧ǫǫ̀ǫ́ǫ̂ǫ̃ǭǭ̀ǭ́ǭ̂ǭ̃ǭ̆ǭ̌ǫ̆́ǫ̆́ǫ̇́ǫ̇́ǫ̈̀ǫ̈̀́ǫ̈́̂ǫ̈̂̄ǫ̈̄̌ǫ̈̌ǫ̋ǫ̌ǫ̑ǫ̣ǫ̱́ǫ̱́̀ǫ̱̀ǫ᷎o̭o̰ó̰o̱ò̱ó̱ô̱ǒ̱õ̱ō̱ṓ̱ṑ̱̂ō̱̂ö̱́ö̱́̀ö̱̀̂ö̱̂̌ö̱̌o̮ọọ̀ọ́ộọ̃ọ̄̀ọ̄̀́ọ̄́̃ọ̄̃̆ọ̄̆ọ̆ọ̈̀ọ̈̀́ọ̈́̂ọ̈̂̄ọ̈̄̌ọ̈̌ọ̌ọ̑ợọo̤ò̤ó̤ô̤ö̤o̥ō̥o̬o̯õ͔ō͔o̜o̹ó̹o̲ꝍꝋɔ́ɔ̀ɔ̂ɔ̌ɔ̄ɔ̃́ɔ̃́̀ɔ̃̀̂ɔ̃̂̌ɔ̃̌̍ɔ̃̍ɔ̄ɔ̆ɔ̈̀ɔ̈̀́ɔ̈́̂ɔ̈̂̌ɔ̈̌ɔ̍ɔ̇ɔ̣̀ɔ̣̀́ɔ̣́̂ɔ̣̂̌ɔ̣̌̈ɔ̣̈̈̀ɔ̣̈̀̈́ɔ̣̈́̈̂ɔ̣̈̂̈̌ɔ̣̈̌̃ɔ̣̃ɔ̤̀ɔ̤̀́ɔ̤́̂ɔ̤̂̈ɔ̤̈ɔ̱̀ɔ̱̀́ɔ̱́̂ɔ̱̂̌ɔ̱̌̃ɔ̱̃̈ɔ̱̈̈̀ɔ̱̈̀̈́ɔ̱̈́ɔ̧́ɔ̧́̀ɔ̧̀̂ɔ̧̂̌ɔ̧̌ɔ̨́ɔ̨́̀ɔ̨̀̂ɔ̨̂̌ɔ̨̌̄ɔ̨̄̆ɔ̨̆̈ɔ̨̈ɔ̱',
'p':'p̀ṕp̃p̄p̆ṗp̈p̋p̑p̓p̕p̔p͑p̱p̣p̤p̬ᵽꝑƥꝓꝕ',
'q':'q́q̃q̄q̇q̈q̋q̓q̕q̧q̣̇q̣̇̈q̣̈q̱ꝗꝗ̃ꝙɋ',
'r':'r̀ŕr̂r̃r̄r̆ṙr̋řr̍ȑȓr̓r̕ŗr̦r̨̄r̨̄ꞧr̭ṟṛṛ̀ṛ́ṝṝ́ṝ̃ṝ̆r̤r̥̀r̥̀ŕ̥̂r̥̂̃r̥̃̄r̥̄̄́r̥̄́̄̆r̥̄̆ř̥r̬r̩r̯ɍɽꝛ́ꝛ̣',
's':'s̀śś̀śṥŝs̃s̄s̆ṡṡ̃s̈s̋šš̀š́ṧš̓s̑s̓s̕şșs̨š̨ꞩs̱ś̱s̮ṣṣ́ṣ̄ṩṣ̌ṣ̕ṣ̱s̤š̤s̥ś̥s̬s̪ᵴȿ',
't':'t̀t́t̃t̄t̆̀t̆̀ṫẗťt̑t̓t̕t̔t͑ţțt̨t̗ṱt̰ṯt̮ṭṭ́t̤t̥t̬t̯t̪ŧⱦƭʈ',
'u':'ùúûũũ̀ṹũ̂ũ̊ũ̌ũ̍ūū̀ū́ū̂ū̌ū̃ū̄ū̆́ū̆́ṻŭŭ̀ŭ́u̇́u̇́̄u̇̄üǜǘü̂ü̃ǖǖ̆ü̆ǚủůů́ů̃űǔu̍ȕȗu̓u᷎ủưứừữửựu̧ú̧ù̧û̧ǔ̧ųų̀ų́ų̂ų̌ų̄́ų̄́̀ų̄̀̂ų̄̂̌ų̄̌̌ų̄̌ų̈́ų̈́̀ų̈̀̂ų̈̂̌ų̈̌̄ų̈̄ų̋ų̱́ų̱́̀ų̱̀ṷṵṵ́ṵ̈u̱ù̱ú̱û̱ũ̱ū̱́ū̱́̀ū̱̀̂ū̱̂ü̱ǘ̱ǜ̱̂ü̱̂ǚ̱ǔ̱ụụ̀ụ́ụ̂ụ̃ụ̄ụ̈̀ụ̈̀́ụ̈́̂ụ̈̂̌ụ̈̌ụ̌ụ̍ṳṳ̀ṳ́ṳ̂ṳ̈u̥ü̥u̯ũ̯ü̯u͔ũ͔ū͔ʉʉ̀ʉ́ʉ̂ʉ̃ʉ̄ʉ̈ʉ̌ʉ̧ʉ̰́ʉ̰́ʉ̱́ʉ̱́̀ʉ̱̀̂ʉ̱̂̈ʉ̱̈̌ʉ̱̌ʉ̥',
'v':'v̀v́v̂ṽṽ̀ṽ́ṽ̂ṽ̌v̄̀v̄̀́v̄́̂v̄̂̃v̄̃̄v̄̄̆v̄̆̌v̄̌v̆́v̆́v̇v̈̀v̈̀́v̈́̂v̈̂̄v̈̄̌v̈̌v̊v̋v̌v̍v̏v̐v̓v̧v̨̀v̨̀́v̨́̂v̨̂̌v̨̌̄v̨̄̄́v̨̄́̄̀v̨̄̀̄̂v̨̄̂̄̌v̨̄̌̈v̨̈̈́v̨̈́̈̀v̨̈̀̈̂v̨̈̂̈̌v̨̈̌̈̄v̨̈̄̋v̨̱̋v̨̱̱́v̨̱̱́̀v̨̱̱̀̂v̨̱̱̂̌v̨̱̌v̱̀v̱̀́v̱́̂v̱̂̌v̱̌ṽ̱̈v̱̈̈́v̱̈́̈̀v̱̈̀̈̂v̱̈̂̈̌v̱̈̌ṿv̥ꝟʋꝩ́ꝩ̇ꝩ̣',
'w':'ẁẃŵw̃w̄w̆ẇẅẘw̋w̌w̍w̓w̱ẉw̥w̬ⱳ',
'x':'x̀x́x̂x̃x̄x̆́x̆́ẋẍx̊x̌x̓x̕x̱̓x̱̓x̣̓x̣̓x̥',
'y':'ỳýŷỹȳȳ̀ȳ́ȳ̃ȳ̆y̆̀y̆̀́y̆́ẏẏ́ÿÿ́ẙy̋y̌y̍y̐y̓ỷy᷎y̱ỵỵ̣y̥y̯ɏƴỿ',
'z':'z̀źẑz̃z̄żz̈z̋žž́ž̏z̑z̓z̕z̨z̗ẕz̮ẓẓ́ẓ̌ẓ̣z̤z̥ƶȥɀⱬʒ́ʒ̇ǯǯ́ʒ̥',
'_':'þ́þ̣ꝥꝧꜯ'
}


_orig = ''
_trans = ''
for key in asciiequivs:
  for char in asciiequivs[key]:
    _orig += char
    _trans += key
ASCIITRANS = str.maketrans(_orig, _trans)


