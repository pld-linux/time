Summary:     	GNU time Utility
Summary(de): 	GNU-Time-Utility 
Summary(fr): 	Utilitaire time de GNU
Summary(pl): 	Narzêdzie do pomiaru czasu GNU
Summary(tr): 	GNU zamanlama aracý
Name: 	     	time
Version:     	1.7
Release:     	11
Copyright:   	GPL
Group: 	     	Utilities/System
Group(pl):	Narzêdzia/System
Source:      	ftp://prep.ai.mit.edu/pub/gnu/time/%{name}-%{version}.tar.gz
Patch0:      	time-info.patch
Patch1:      	time-man.patch
Buildroot:   	/tmp/%{name}-%{version}-root

%description
The 'time' utility is used as a sort of 'stopwatch' to time the execution
of a specified command. It can aid in the optimization of programs for
maximum speed, as well as a number of other uses.

%description -l de
Das TIME-Utility wird als eine Art Stoppuhr zum Messen der Ausführung eines
bestimmten Befehls benutzt. Es dient in erster Linie der Optimierung von
Programmen für maximale Geschwindigkeit, hat aber daneben eine Vielzahl
anderer Anwendungen. 

%description -l fr
L'utilitaire « time » sert de chronomètre pour mesurer le temps d'exécution
d'une commande donnée. Il peut aider à l'optimisation de programmes pour
obtenir une vitesse maximale et a beaucoup d'autres uilisations.

%description -l pl
Program time umo¿liwia zmierzenie czasu wykonania badanego programu.
Jest pomocne np. przy optymalizowaniu algorytmów pod k±tem szybko¶ci.

%description -l tr
time, bir uygulamanýn çalýþma zamanýnýn ölçülmesi için kronometre gibi
kullanýlýr. Genellikle programlarýn hýz açýsýndan iyileþtirilmesinde
yararlý olur.

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
/sbin/install-info %{_infodir}/time.info.gz /etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/time.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) %{_bindir}/time

%{_infodir}/time.info*
%{_mandir}/man1/*

%changelog
* Mon May 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-10]
- more rpm macros.

* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.7-9]
- gzipped docs
- compiled on rpm 3

* Mon Dec 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-8]
- standarized {un}registering info pages (added time-info.patch),
- added useing "make install" in %install,
- added gzipping man pages.

* Mon Dec 14 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-7]
- added "Prereq: /sbin/install-info",
- standarized {un}registering info pages.

* Sat Oct 10 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- allow building from non root account,
- build against GNU libc-2.1.
