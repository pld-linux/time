Summary:	GNU time Utility
Summary(de.UTF-8):	GNU-Time-Utility
Summary(fr.UTF-8):	Utilitaire time de GNU
Summary(pl.UTF-8):	Narzędzie GNU do pomiaru czasu
Summary(tr.UTF-8):	GNU zamanlama aracı
Name:		time
Version:	1.9
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/time/%{name}-%{version}.tar.gz
# Source0-md5:	d2356e0fe1c0b85285d83c6b2ad51b5f
Patch0:		%{name}-info.patch
Patch1:		%{name}-man.patch
URL:		http://www.gnu.org/software/time/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'time' utility is used as a sort of 'stopwatch' to time the
execution of a specified command. It can aid in the optimization of
programs for maximum speed, as well as a number of other uses.

%description -l de.UTF-8
Das TIME-Utility wird als eine Art Stoppuhr zum Messen der Ausführung
eines bestimmten Befehls benutzt. Es dient in erster Linie der
Optimierung von Programmen für maximale Geschwindigkeit, hat aber
daneben eine Vielzahl anderer Anwendungen.

%description -l fr.UTF-8
L'utilitaire « time » sert de chronomètre pour mesurer le temps
d'exécution d'une commande donnée. Il peut aider à l'optimisation de
programmes pour obtenir une vitesse maximale et a beaucoup d'autres
uilisations.

%description -l pl.UTF-8
Program time umożliwia zmierzenie czasu wykonania badanego programu.
Jest pomocny np. przy optymalizowaniu algorytmów pod kątem szybkości.

%description -l tr.UTF-8
time, bir uygulamanın çalışma zamanının ölçülmesi için kronometre gibi
kullanılır. Genellikle programların hız açısından iyileştirilmesinde
yararlı olur.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p time.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/time
%{_infodir}/time.info*
%{_mandir}/man1/time.1*
