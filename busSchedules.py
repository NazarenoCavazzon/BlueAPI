# ====================== Horarios Linea 1B ======================
schedule1B = [
    ["Crucero","07:20","08:20","09:30","10:30","11:40","12:50","14:00","16:15","17:15","18:20","19:30"],
    ["Centro","07:30","08:30","09:40","10:40","11:50","13:00","14:10","16:25","17:25","18:30","19:40"],
    ["Esc Yrigoyen","","","","","12:00","","","","17:30","",""],
    ["Esc Padre Viera","07:40","08:40","09:50","10:50","","13:10","14:20","16:35","","18:40","19:50"],
    ["La Perla",'07:45', '08:45', '09:55', '10:55', '12:10', '13:15',"14:25", '16:40', '17:40', '18:45', '19:50'],
    ["Crucero Sud", '', '08:50', '', '', '12:15', '',"", '16:45', '', '', '20:00'],
    ["La Perla",'07:45', '08:55', '09:55', '10:55', '12:20', '13:15',"14:25", '16:50', '17:40', '18:45', '20:05'],
    ["Esc Padre Viera",'', '09:00', '10:00', '11:00',"12:25", '', '14:30', '16:55', '17:45', '18:55', '20:10'],
    ["Esc Yrigoyen",'07:50', '', '', '',"", '13:25', '', '', '', '', ''],
    ["Centro", '08:05', '09:10', '10:10', '11:10',"12:35", '13:35', '14:40', '17:05', '17:55', '19:05', '20:20'],
    ["Crucero",'08:20', '09:25', '10:25', '11:25', '12:50', '13:50',"15:00", '17:15', '18:10', '19:20', '20:30']
]

# ====================== Horarios Linea 2 ======================
schedule2 = [
    ['Terminal','','', '07:20','08:05', '08:50', '09:35','10:20', '11:05','11:55',"12:40", '13:25', '14:10', '14:55', '16:28','17:58', '19:28', '20:58',"SABADOS",'','09:15', '10:35', '12:00', '13:20', '14:45',"16:15", '17:40', '19:02'],
    ['Centro','','', '07:26','08:11','08:56', '09:41','10:26', '11:11','12:01',"12:46", '13:31', '14:16', '15:01', '16:34','18:04', '19:34', '21:04',"DOMINGOS",'','09:20', '10:40', '12:05', '13:25', '14:50',"16:20", '17:45', '19:07'],
    ['Barrio Sur','','06:38', '07:32','08:17','09:02', '09:47','10:32', '11:17','12:07',"12:52", '13:37', '14:22', '15:07', '16:40','18:10', '19:40', '21:10',"Y FERIADOS",'','09:25', '10:45', '12:10', '13:30', '14:55',"16:25", '17:50', '19:12'],
    ['Villa Oviedo', '06:00','06:45', '07:39','08:26','09:09', '09:54','10:39', '11:24','12:14',"12:59", '13:44', '14:29', '15:14', '16:47','18:17', '19:47', '21:17',"↓",'08:07','09:32', '10:52', '12:17', '13:37', '15:02',"16:32", '17:57', '19:19'],
    ['La Perla','06:09',"06:54", '07:48','08:35','09:18', '10:03','10:48', '11:33','12:23',"13:08", '13:53', '14:38', '15:23', '16:56','18:26', '19:56', '21:26',"↓",'08:15','09:40', '11:00', '12:25', '13:45', '15:10',"16:40", '18:05', '19:27'],
    ['Gral Bustos','06:15',"07:00",'07:54','08:41','09:24', '10:09','10:54', '11:39','12:29',"13:14", '13:59', '', '15:29', '17:02','18:32', '20:02', '21:32',"↓",'08:20','09:45', '11:05', '12:30', '13:50', '15:15',"16:45", '18:10', '19:32'],
    ["Barrio Liniers","06:21","07:06","","","","","","","","","","","","","","","","↓","","","","","","","","",""],
    ['Terminal','06:26',"07:11",'08:00','08:45','09:30', '10:15','11:00', '11:45','12:35',"13:20", '14:05', '', '15:35', '17:08','18:38', '20:08', '21:38',"↓",'08:30','09:50', '11:10', '12:35', '13:55', '15:20',"16:50", '18:15', '19:37'],
    ['Centro','06:32',"07:17",'08:06','08:51','09:36', '10:21','11:06', '11:51','12:41',"13:26", '14:11', '', '15:41', '17:14','18:44', '20:14', '21:44',"↓",'08:35','09:55', '11:15', '12:40', '14:00', '15:25',"16:55", '18:20', '19:42'],
    ['Hospital','06:46',"07:31",'08:20','09:05','09:50', '10:35','11:20', '12:05','12:55',"13:40", '14:25', '', '15:55', '17:28','18:58', '20:28', '21:58',"↓",'08:48','10:08', '11:28', '12:53', '14:13', '15:38',"17:08", '18:33', '19:55'],
    ['Crucero','06:49',"07:34",'08:23','09:08','09:53', '10:38','11:23', '12:08','12:58',"13:43", '14:28', '', '15:58', '17:31','19:01', '20:31', '22:00',"↓",'08:50','10:10', '11:30', '12:55', '14:15', '15:40',"17:10", '18:35', '19:57'],
    ['Cementerio','',"", '08:25','09:10','09:55', '10:40','11:25', '12:10','13:00',"13:45", '14:30', '', '16:00', '17:33','19:03', '20:33', '',"↓",'08:52','10:12', '11:32', '12:57', '14:17', '15:42',"17:12", '18:37', ''],
    ['Hospital (Al Centro)','06:54',"07:40", '08:30','09:15','10:00', '10:45','11:30', '12:15','13:05',"13:50", '14:35', '', '16:05', '17:38','19:08', '20:38', '',"SABADOS",'08:56','10:16', '11:36', '13:01', '14:21', '15:46',"17:16", '18:41', ''],
    ['Centro','07:10',"07:54",'08:45','09:30','10:15', '11:00','11:45', '12:30','13:20',"14:05", '14:50', '', '16:20', '17:52','19:22', '20:52', '',"DOMINGOS",'09:10','10:30', '11:50', '13:15', '14:35', '16:00',"17:30", '18:55', ''],
    ['Terminal','07:15','08:00', '08:50', '09:35','10:20', '11:05','11:55',"12:40", '13:25', '14:10', '14:55',"", '16:25','17:58', '19:28', '20:58', '',"Y FERIADOS",'09:15','10:35', '11:55', '13:20', '14:40', '16:05',"17:35", '19:00', ''],
]

# ====================== Horarios Linea 3 ======================
schedule3 = [
    ["B° Virrey","06:05","06:40","07:19","08:04","08:51","09:20","10:18","10:41","11:34","12:08","12:50","13:35","15:02","16:25","17:41","19:08","20:35","HORARIOS","09:10","11:40","14:05","16:30","19:00"],
    ["Centro","06:25","07:00","07:39","08:24","09:11","09:40","10:38","11:01","11:54","12:28","13:10","13:55","15:22","16:45","18:01","19:28","20:55","SABADOS Y","09:30","12, 00","14:25","16:50","19:20"],
    ["B° Cordoba","06:30","07:05","07:44","08:29","09:16","09:45","10:43","11:06","11:59","12:33","13:15","14:00","15:27","16:50","18:06","19:33","21:00","DOMINGOS","09:35", "12:05", "14:30","16:55","19:25"],
    ["Portales del Sol","","07:10","07:49","","09:21","","","11:11","","12:38","13:20","14:05","","","18:11","19:38","","--------","09:41","12:11","14:36","17:01","19:31"],
    ["Villa Camiares","","07:15","07:54","","09:27","","","11:17","","12:44","13:26","14:11","","","18:16","19:43","","HORARIOS","09:45","12:15","14:40","17:05","19:35"],
    ["B° Sabattini","06:40","07:25","08:04","08:39","09:37","09:55","10:53","11:27","12:09","12:54","13:36","14:21","15:37","17:00","18:27","19:54","21:10","SABADOS Y","09:55","12:25","14:50","17:15","19:45"],
    ["Centro","06:55","07:40","08:20","08:54","09:52","10:10","11:08","11:42","12:24","13:09","13:51","14:36","15:52","17:15","18:42","20:09","21:25","DOMINGOS","10:10","12:40","15:05","17:30","20:00"],
    ["Hospital","07:06","07:51","08:31","09:05","10:03","10:21","11:19","11:53","12:35","13:20","14:02","14:47","16:03","17:26","18:53","20:20","21:36","--------","10:20","12:50","15:15","17:40","20:10"],
    ["Crucero","07:09","07:54","08:34","09:08","10:06","10:24","11:22","11:56","12:38","13:23","14:05","14:50","16:06","17:29","18:56","20:23","21:39","HORARIOS","10:25","12:55","15:20","17:45","20:15"],
    ["Cementerio","","","08:36","09:10","10:08","10:26","11:24","11:58","12:40","13:25","","14:52","16:08","17:31","18:58","20:25","","SABADOS Y","","","","",""],
    ["B° Virrey","07:19","08:04","08:46","09:20","10:18","10:36","11:34","12:08","12:50","13:35","","15:02","16:18","17:41","19:08","20:35","","DOMINGOS","10:30","13:00","15:25","17:50","20:20"],
]

# ====================== Horarios Linea 4 ======================
schedule4 = [
    ["B° Virrey","07:00","07:35","08:15","08:51","09:30","10:06","10:41","11:17","11:56","12:28","13:07","13:43","14:18","15:33","16:50","18:01","19:16","20:27","HORARIOS","08:05","10:35","13:00","15:25","17:50"],
    ["Centro","07:21","07:56","08:36","09:12","09:51","10:27","11:02","11:38","12:17","12:49","13:28","14:04","14:39","15:54","17:11","18:22","19:37","20:48","SABADOS","08:25","10:55","13:20","15:45","18:10"],
    ["Terminal","07:31","08:06","08:46","09:22","10:01","10:37","11:12","11:48","12:27","12:59","13:38","14:14","14:49","16:04","17:21","18:32","19:47","20:58","DOMINGOS","08:35","11:05","13:30","15:55","18:20"],
    ["B° Tiro Federal","07:35","","","09:26","","","11:16","","","13:03","","","14:53","","","18:36","","","----------","","","","",""],
    ["B° Liniers","07:41","08:12","08:52","09:32","10:07","10:43","11:22","11:54","12:33","13:09","13:44","14:20","14:59","16:10","17:27","18:42","19:53","21:04","HORARIOS","08:40","11:10","13:35","16:00","18:25"],
    ["Centro","07:53","08:24","09:04","09:44","10:19","10:55","11:34","12:06","12:45","13:21","13:56","14:32","15:11","16:22","17:39","18:54","20:05","21:16","SABADOS","08:50","11:20","13:45","16:10","18:35"],
    ["B° Virrey","08:15","08:51","09:26","10:06","10:41","11:17","11:56","12:28","13:07","13:43","14:18","14:54","15:33","16:44","18:01","19:16","20:27","21:38","DOMINGOS","09:10","11:40","14:05","16:30","18:55"],
]

# ====================== Horarios Linea 5 ======================
schedule5 = [
    ["Crucero","06:20","07:00","07:40","08:20","09:00","09:40","10:20","11:00","11:40","12:20","13:00","13:40","14:40","15:20","16:00","16:40","17:20","18:00","18:40","19:20","20:00","20:40"],
    ["B° Don Bosco","06:37","07:17","07:57","08:37","09:17","09:57","10:37","11:17","11:57","12:37","13:17","13:57","14:57","15:37","16:17","16:57","17:37","18:17","18:57","19:37","20:17","20:57"],
    ["Plaza Solares","06:55","07:35","08:15","08:55","09:35","10:15","10:55","11:35","12:15","12:55","13:35","14:15","15:15","15:55","16:35","16:15","17:55","18:35","19:15","19:55","20:35","21:15"],
    ["Colonia J.M. Paz","07:05","07:45","08:25","09:05","09:45","10:25","11:05","11:45","12:25","13:05","13:45","14:25","15:25","16:05","16:45","17:25","18:05","18:45","19:25","20:05","20:45","21:25"],
    ["Plaza Solares","07:20","08:00","08:40","09:20","10:00","10:40","11:20","12:00","12:40","13:20","14:00","14:40","15:40","16:20","17:00","17:40","18:20","19:00","19:40","20:20","21:00","21:40"],
    ["B° Don Bosco","07:30","08:10","08:50","09:30","10:10","10:50","11:30","12:10","12:50","13:30","14:10","14:50","15:53","16:33","17:13","17:53","18:33","19:13","19:53","20:33","21:13","21:53"],
    ["Crucero","07:40","08:20","09:00","09:40","10:20","11:00","11:40","12:20","13:00","13:40","14:20","15:00","16:00","16:40","17:20","18:00","18:40","19:20","20:00","20:40","21:20","22:00"],
]

# ====================== Horarios Linea 6 ======================
schedule6 = [
    ["Paravachasca","06:20","06:55","07:34","08:15","08:54","09:30","10:08","10:43","11:28","12:03","12:42","13:17","13:56","15:10","16:30","17:44","19:04","20:18"],
    ["B° Sabattini","06:30","07:05","07:44","08:25","09:04","09:40","10:18","10:53","11:38","12:13","12:52","13:27","14:06","15:20","16:40","17:54","19:14","20:28"],
    ["Centro","06:40","07:15","07:54","08:35","09:14","09:50","10:28","11:03","11:48","12:23","13:02","13:37","14:16","15:30","16:50","18:04","19:24","20:38"],
    ["Hospital","06:51","07:26","08:05","08:46","09:25","10:01","10:39","11:14","11:59","12:34","13:13","13:48","14:27","15:41","17:01","18:15","19:35","20:49"],
    ["B° Parque San Juan","06:56","07:37","08:16","08:51","09:30","10:06","10:50","11:25","12:04","12:39","13:18","13:53","14:32","15:52","17:06","18:26","19:40","20:54"],
    ["Cementerio","07:01","07:42","08:21","08:56","09:35","10:10","10:55","11:30","12:09","12:44","13:23","","14:37","15:57","17:11","18:31","19:45",""],
    ["Hospital","07:05","07:46","08:25","09:00","09:39","10:14","10:59","11:34","12:13","12:48","13:27","","14:41","16:01","17:15","18:35","19:49",""],
    ["Centro","07:18","07:59","08:38","09:13","09:52","10:27","11:12","11:47","12:26","13:01","13:40","","14:54","16:14","17:28","18:48","20:02",""],
    ["B° Sabattini","07:29","08:10","08:49","09:24","10:03","10:38","11:23","11:58","12:37","13:12","13:51","","15:05","16:25","17:39","18:59","20:13",""],
    ["Paravachasca","07:34","08:15","08:54","09:30","10:08","10:43","11:28","12:03","12:42","13:17","13:56","","15:10","16:30","17:44","19:04","20:18",""]
]

# ====================== Horarios Linea 7 ======================
horario7 = [
    ["Villa Camiares","","07:37","09:14","10:51","12:34"],
    ["Paravachasca","","07:47","09:24","11:01","12:44"],
    ["B° Cordoba","","07:52","09:29","11:06","12:49"],
    ["B° Pellegrini","","07:59","09:36","11:13","12:56"],
    ["Terminal","","08:03","09:40","11:17","13:00"],
    ["B° Liniers","","08:06","09:43","11:20","13:03"],
    ["B° Gral Bustos","","08:11","09:48","11:25","13:08"],
    ["Centro","","08:16","09:54","11:29","13:13"],
    ["B° Norte","","08:18","09:56","11:31","13:15"],
    ["B° Santa Maria","06:40","08:23","10:00","11:37","13:20"],
    ["B° Virrey","06:44","08:27","10:04","11:41","13:24"],
    ["B° Camara","06:48","08:31","10:08","11:45","13:29"],
    ["Crucero","07:00","08:37","10:14","11:57","13:34"],
    ["B° Camara","07:06","08:43","10:20","12:03","13:40"],
    ["B° Norte","07:11","08:48","10:25","12:08","13:45"],
    ["B° Gral Bustos","07:17","08:54","10:31","12:12","13:51"],
    ["B° Liniers","07:22","09:01","10:36","12:17","13:56"],
    ["Terminal","07:25","09:04","10:39","12:20","13:59"],
    ["B° Pellegrini","07:28","09:07","10:42","12:23","14:02"],
    ["Villa Camiares","07:37","09:14","10:51","12:34","14:11"]
]

# ====================== Horario Sarmiento a Carlos Paz ======================
horario242 = [
    ["Carlos Paz","06:15","08:50","11:15","16:45","20:55"],
    ["San Nicolas","06:30","09:05","11:30","17:00","21:10"],
    ["Cruce R20","06:34","09:10","11:35","17:05","21:15"],
    ["La Juanita","06:45","X","11:45","X","X"],
    ["F. del Cañete","06:50","09:18","11:50","17:15","21:25"],
    ["F. del Carmen","07:00","09:27","12:00","17:25","21:32"],
    ["Valle Alegre","07:02","09:32","12:02","17:28","21:35"],
    ["Alta Gracia (Llega)","07:15","09:45","12:20","17:45","21:50"],
    ["Alta Gracia (Sale)","07:30","10:10","12:40","15:30","19:50"],
    ["Valle Alegre","07:45","10:25","12:55","15:45","20:05"],
    ["F. del Carmen","07:50","10:30","12:58","15:48","20:08"],
    ["F. del Cañete","07:58","10:38","13:07","15:55","20:15"],
    ["La Juanita","08:05","X","13:12","X","X"],
    ["Cruce R20","08:13","10:46","13:20","16:05","20:25"],
    ["San Nicolas","08:18","10:51","13:25","16:10","20:30"],
    ["Carlos Paz Llega","08:40","11:05","13:40","16:25","20:45"]
]

# ============= Horario Sierras de Calamuchita ==============
horariosierras = [
        ["Cordoba", "00:30", "06:00", "06:20", "06:40", "07:10", "07:45", "08:15", "08:40", "09:05", "09:30", "10:00", "10:20", "10:45", "11:10", "11:30", "11:50", "12:00", "12:15", "12:30", "12:45", "13:00", "13:20", "13:40", "14:00", "14:20", "14:45", "15:10", "15:30", "15:50", "16:10", "16:30", "16:45", "17:00", "17:20", "17:40", "18:00", "18:25", "18:45", "19:05", "19:30", "20:00", "20:20", "20:45", "21:10", "21:30", "22:15", "23:00"],
        ["Santa Ana", "01:10", "06:40", "07:00", "07:20", "07:50", "08:25", "08:55", "09:20", "09:45", "10:10", "10:40", "11:00", "11:15", "11:50", "12:10", "12:30", "12:40", "12:55", "13:10", "13:25", "13:40", "14:00", "14:20", "14:40", "15:00", "15:25", "15:50", "16:10", "16:30", "16:50", "17:10", "17:25", "17:40", "18:00", "18:20", "18:40", "19:05", "19:25", "19:45", "20:10", "20:40", "21:00", "21:25", "21:50", "22:10", "22:55", "23:40"],
        ["Alta Gracia (llega)", "01:40", "07:05", "07:25", "07:45", "08:15", "08:50", "09:20", "09:45", "10:10", "10:35", "11:05", "11:25", "11:50", "12:15", "12:35", "12:55", "13:05", "13:20", "13:35", "13:50", "14:05", "14:25", "14:45", "15:05", "15:25", "15:50", "16:15", "16:35", "16:55", "17:15", "17:35", "17:50", "18:05", "18:25", "18:45", "19:05", "19:30", "19:50", "20:10", "20:35", "21:05", "21:25", "21:50", "22:15", "22:35", "23:20", "00:05"],
        ["Alta Gracia (sale)", "00:10*", "05:00", "05:30", "06:10", "06:20", "06:30", "06:40", "07:10", "07:20", "07:35", "07:50", "08:20", "08:40", "09:10", "09:30", "10:00", "10:30", "10:50", "11:20", "11:40", "12:05", "12:30", "13:00", "13:30", "13:50", "14:10", "14:40", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "17:45", "18:00", "18:30", "19:00", "19:20", "19:40", "20:00", "20:30", "21:00", "21:30", "22:10", "23:00"],
        ["Santa Ana", "00:35", "05:25", "05:55", "06:00", "06:36", "06:56", "07:02", "07:06", "07:27", "07:37", "07:47", "08:06", "08:16", "08:47", "09:07", "09:36", "09:58", "10:25", "10:55", "11:15", "11:46", "12:07", "12:32", "12:58", "13:27", "13:57", "14:17", "14:35", "15:05", "15:25", "15:55", "16:25", "16:55", "17:25", "17:55", "18:10", "18:25", "18:55", "19:25", "19:45", "20:05", "20:25", "20:55", "21:25", "21:55", "22:35", "23:25"]
]

# ============= Horario Sarmiento Diferencial ==============
horarioSarmientoDif = [
        ["Alta Gracia", "05:50", "06:20", "06:50", "07:20", "07:50", "08:20", "09:20", "09:50", "10:20", "10:50", "11:20", "11:50", "12:50", "14:10", "15:30", "16:10", "16:40", "17:10", "17:40", "18:10", "18:40", "19:10", "19:40", "20:10", "22:00"],
        ["Córdoba", "06:55", "07:25", "07:55", "08:25", "08:55", "09:25", "10:25", "10:55", "11:25", "11:55", "12:25", "12:55", "13:55", "15:15", "16:35", "17:15", "17:45", "18:15", "18:45", "19:15", "19:45", "20:15", "20:45", "21:15", "23:00"],
        ["Córdoba (sale)", "07:05", "07:35", "08:05", "08:35", "09:05", "09:35", "10:35", "11:05", "11:35", "12:05", "12:35", "13:05", "14:05", "15:25", "16:45", "17:25", "17:55", "18:25", "18:55", "19:25", "19:55", "20:25", "20:55", "21:20", "23:00"],
        ["Alta Gracia (llega)", "08:10","08:40","09:10", "09:40", "10:10", "10:40", "11:40","12:10", "12:40","13:10","13:40", "14:10", "15:10", "16:30", "17:50", "18:30", "19:00", "19:30", "20:00", "20:30","21:00","21:30", "22:00","22:20","00:00"]
]

# ============= Horario Sarmiento Cba x Falda del Carmen =============
horarioS2 = [
    ["Alta Gracia", "06:00"],
    ["Cordoba", "07:30"]
]
