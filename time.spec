Summary:	GNU time Utility
Summary(de):	GNU-Time-Utility 
Summary(fr):	Utilitaire time de GNU
Summary(pl):	Narz�dzie do pomiaru czasu GNU
Summary(tr):	GNU zamanlama arac�
Name:		time
Version:	1.7
Release:	14
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://prep.ai.mit.edu/pub/gnu/time/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-man.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'time' utility is used as a sort of 'stopwatch' to time the
execution of a specified command. It can aid in the optimization of
programs for maximum speed, as well as a number of other uses.

%description -l de
Das TIME-Utility wird als eine Art Stoppuhr zum Messen der Ausf�hrung
eines bestimmten Befehls benutzt. Es dient in erster Linie der
Optimierung von Programmen f�r maximale Geschwindigkeit, hat aber
daneben eine Vielzahl anderer Anwendungen.

%description -l fr
L'utilitaire � time � sert de chronom�tre pour mesurer le temps
d'ex�cution d'une commande donn�e. Il peut aider � l'optimisation de
programmes pour obtenir une vitesse maximale et a beaucoup d'autres
uilisations.

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
autoconf
%configure

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

install time.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf NEWS README

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) %{_bindir}/time

%{_infodir}/time.info*
%{_mandir}/man1/*
