class Migration_Dispositivos:
    def Table_Dispositivos():
        return '''
CREATE TABLE IF NOT EXISTS `dispositivos` (
  `id` int NOT NULL,
  `Wifi_MacAddress` varchar(18) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`));
'''