param(
  [Parameter(Mandatory=$true)][string]$List,    # text file: lines of "name<TAB or spaces>url"
  [Parameter(Mandatory=$true)][string]$Outdir
)
$ProgressPreference = 'SilentlyContinue'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -ItemType Directory -Force -Path $Outdir | Out-Null
Get-Content $List | ForEach-Object {
  $line = $_.Trim()
  if ($line -eq '' -or $line.StartsWith('#')) { return }
  $idx = $line.IndexOf(' ')
  if ($idx -lt 1) { return }
  $name = $line.Substring(0, $idx)
  $url  = $line.Substring($idx + 1).Trim()
  $ext  = if ($url -match '\.png(\?|$)') { 'png' } else { 'jpg' }
  $dest = Join-Path $Outdir ("$name.$ext")
  try {
    Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $dest -TimeoutSec 30
    Write-Output ("OK  " + $dest)
  } catch {
    Write-Output ("FAIL " + $name + " : " + $_.Exception.Message)
  }
}
