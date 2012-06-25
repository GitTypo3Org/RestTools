<?php
  /***************************************************************
   *  Copyright notice
   *
   *  (c) 2010 Kai Vogel <kai.vogel@speedprogs.de>
   *  All rights reserved
   *
   *  This script is part of the TYPO3 project. The TYPO3 project is
   *  free software; you can redistribute it and/or modify
   *  it under the terms of the GNU General Public License as published by
   *  the Free Software Foundation; either version 2 of the License, or
   *  (at your option) any later version.
   *
   *  The GNU General Public License can be found at
   *  http://www.gnu.org/copyleft/gpl.html.
   *
   *  This script is distributed in the hope that it will be useful,
   *  but WITHOUT ANY WARRANTY; without even the implied warranty of
   *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   *  GNU General Public License for more details.
   *
   *  This copyright notice MUST APPEAR in all copies of the script!
   ***************************************************************/

  // Check params
  if (empty($argv) || count($argv) < 3) {
    die('Usage: php ext_decompress.php <source> <target>' . PHP_EOL);
  }

  // Get source file
  $sSource = $argv[1];
  if (!file_exists($sSource) || strpos($sSource, '.t3x') === FALSE) {
    die('Source is not a valid t3x file!' . PHP_EOL);
  }

  // Get target path
  $sPath = $argv[2];
  if (!is_dir($sPath)) {
    die('Target path does not exist!' . PHP_EOL);
  }
  $sPath = rtrim($sPath, '/') . '/';

  // Get file contents
  $sContent = file_get_contents($sSource);
  $aParts   = explode(':', $sContent, 3);
  $sData    = $aParts[2];

  // Decompress
  if ($aParts[1] == 'gzcompress') {
    $sData = gzuncompress($aParts[2]);
  }

  // Check if file content is valid
  if (md5($sData) != $aParts[0]) {
    die('Extension file is not valid!' . PHP_EOL);
  }

  // Get extension data
  $aData = unserialize($sData);
  if (!is_array($aData)) {
    die('Could not unserialize extension data!' . PHP_EOL);
  }

  // Create extension folder if not exists
  $sExtPath = $sPath . $aData['extKey'] . '/';
  if (!is_dir($sExtPath)) {
    @mkdir($sExtPath, 0777, TRUE);
  }

  // Create all folders and files
  foreach ($aData['FILES'] as $sFileName => $aConf) {
    if (!is_array($aConf)) {
      echo('No valid data for file "' . $sFileName . '" found!');
      continue;
    }

    // Create folders
    if (strpos($sFileName, '/') !== FALSE) {
      @mkdir($sExtPath . dirname($sFileName), 0777, TRUE);
    }

    // Create file...
    file_put_contents($sExtPath . $sFileName, $aConf['content']);
  }
?>