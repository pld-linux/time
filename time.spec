Summary:     	GNU time Utility
Summary(de): 	GNU-Time-Utility 
Summary(fr): 	Utilitaire time de GNU
Summary(pl): 	Narz�dzie do pomiaru czasu GNU
Summary(tr): 	GNU zamanlama arac�
Name: 	     	time
Version:     	1.7
Release:     	11
Copyright:   	GPL
Group: 	     	Utilities/System
Group(pl):	Narz�dzia/System
Source:      	ftp://prep.ai.mit.edu/pub/gnu/time/%{name}-%{version}.tar.gz
Patch0:      	time-info.patch
Patch1:      	time-man.patch
Prereq:		/usr/sbin/fix-info-dir
Buildroot:   	/tmp/%{name}-%{version}-root

%description
The 'time' utility is used as a sort of 'stopwatch' to time the execution
of a specified command. It can aid in the optimization of programs for
maximum speed, as well as a number of other uses.

%description -l de
Das TIME-Utility wird als eine Art Stoppuhr zum Messen der Ausf�hrung eines
bestimmten Befehls benutzt. Es dient in erster Linie der Optimierung von
Programmen f�r maximale Geschwindigkeit, hat aber daneben eine Vielzahl
anderer Anwendungen. 

%description -l fr
L'utilitaire � time � sert de chronom�tre pour mesurer le temps d'ex�cution
d'une commande donn�e. Il peut aider � l'optimisation de programmes pour
obtenir une vitesse maximale et a beaucoup d'autres uilisations.

%description -l pl
Program time umo�liwia zmierzenie czasu wykonania badanego programu.
Jest pomocne np. przy optymalizowaniu algorytm�w pod k�tem szybko�ci.

%description -l tr
time, bir uygulaman�n �al��ma zaman�n�n �l��lmesi i�in kronometre gibi
kullan�l�r. Genellikle programlar�n h�z a��s�ndan iyile�tirilmesinde
yararl� olur.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
autoconf && %configure

make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    infodir=$RPM_BUILD_ROOT%{_infodir} \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    install 

install time.1 $RPM_BUILD_ROOT%{_mandir}/man1

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/time.info \
	NEWS README $RPM_BUILD_ROOT%{_mandir}/man1/*

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) %{_bindir}/time

%{_infodir}/time.info*
%{_mandir}/man1/*
