% 2023-April-01
%--------------------------------------------
path = 'C:\PyProj\MyScripts\materials\';
file = 'GlassJena_nk.txt';
data = readmatrix( strcat(path,file) );

c = 299792458;
factor = 1e9; % um: 1e6; nm:1e9

freq = flipud( factor*c./data(:,1) ) ;
[ep1,ep2] = n2ep( data(:,2), data(:,3) );
out = [freq,ep1,ep2];
writematrix(out, strcat(path,'dataOut.txt'),'Delimiter','tab');
type 'C:\PyProj\MyScripts\materials\dataOut.txt';
%-------------------------------
function [ep1,ep2] = n2ep(n,k)
    ep1 = flipud(n.^2-k.^2);
    ep2 = flipud(2.*n.*k);
end
