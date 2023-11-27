$exclude = @("venv", "FirstProjetc.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "FirstProjetc.zip" -Force