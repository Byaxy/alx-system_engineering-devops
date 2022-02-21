# fixes Apache 500 error by fixing typo in wordpress
exec { 'fix typo':
  command  => 'sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
  provider => shell
}
