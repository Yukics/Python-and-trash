#Para iniciar el script ejecutar Start-Job switchd.ps1

Try{
    Get-InstalledModule VirtualDesktop 
}
Catch{
    Install-Module VirtualDesktop
}

Import-Module -Force VirtualDesktop 3>$null

#Si queremos agregar programas que no esten bindeados en PS es necesario hacerlo 
#y definir el mismo nombre de alias que de nombre de proceso

#New-Alias -Name chrome -Value "C:\Program Files\Google\Chrome\Application\chrome.exe"

$global:programa = @('explorer','chrome','notepad')

$nprogram = ($programa.count)

#echo $nprogram

#Creacion de los escritorios en funcion de cuantos programas haya en la array
for($i=1; $i -lt $nprogram ; $i++){
    New-Desktop | Out-Null
    #echo "Nuevo escritorio $i"           
}

Start-Process $programa[0]

for($i=1; $i -lt $nprogram ; $i++){
    
    $proc = Start-Process ($programa[$i]) -PassThru
    sleep 6
    (Get-Process -Name $programa[$i]).MainWindowHandle | sort -Descending | select -First 1 | Move-Window (Get-Desktop $i) | Out-Null
    
    #if ($programa[$i] -eq "chrome"){
    #    (Get-Process -Name $programa[$i]).MainWindowHandle | sort -Descending | select -First 1 | Move-Window (Get-Desktop $i) | Out-Null
    #}
    #(Get-Process -Name $proc.ProcessName).MainWindowHandle | sort -Descending | select -First 1 | Move-Window (Get-Desktop $i) | Out-Null
    
    #(Get-Process -Id $proc.Id).MainWindowHandle | Move-Window (Get-Desktop $i) | Out-Null
    #(ps ($programa[$i].Split('\')[-1]).split('\.')[-2])[0].MainWindowHandle | Move-Window (Get-CurrentDesktop) | Out-Null
    #(ps $programa[$i].split('\.')[-2])[0].MainWindowHandle | Move-Window (get-desktop $i.ToString())| Out-Null
    #(ps $programa[$i] | sort -Descending CPU)[0].MainWindowHandle | Move-Window (Get-Desktop $i) | Out-Null
    #Move-ActiveWindow -Desktop (Get-Desktop $i)
    #Find-WindowHandle($programa[$i]) | Move-Window (Get-RightDesktop) | Out-Null
}

#Se puede crear una interrupción del bucle mediante las funciones de datetime

#$hora=Get-Date -Format HH
#$hora=$hora -as [int]
#$hora

$actual=0

while($true){
    Switch-Desktop -Desktop $actual
    echo "Cambio a $actual"
    $actual++
    if ($actual -ge $nprogram){
        $actual=0
    }    
    Start-Sleep 5
}
