Summary:	MPEG audio player
Summary(es):	Ejecuta archivos MP3
Summary(pl):	Odtwarzacz plików audio MPEG
Summary(pt_BR):	Tocador de arquivos MP3
Name:		mpg123
Version:	0.59r
Release:	7
Group:		Applications/Sound
License:	freely distributable for non-commercial use, GPL (mpglib)
Source0:	http://www.mpg123.de/mpg123/%{name}-%{version}.tar.gz
Patch0:		ftp://ftp.kame.net/pub/kame/misc/%{name}-059r-v6-20000111.diff.gz
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-esd.patch
Patch3:		%{name}-audio_sun.patch
URL:		http://www.mpg123.de/
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "mp3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

%description -l es
Ejecuta archivos MP3.

%description -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów unixowych.
Obs³uguje standart MPEG 1.0/2.0 warstwy 1, 2 oraz 3 (s³ynne "mp3"). Do
uzyskania pe³nej jako¶ci CD wymagany jest silny procesor (Pentium,
SPARCstation10, DEC Alpha lub podobny). Ni¿sz± jako¶æ (22 lub 11 kHz)
mo¿na uzyskaæ ju¿ na procesorach 486.

%description -l pt_BR
O mpg123 é um tocador de áudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos .mp3).

%package esd
Summary:	mpg123 for ESD
Summary(pl):	mpg123 dla ESD
Group:		Applications/Sound

%description esd
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "mp3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ESD output.

%description esd -l pl
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików d¼wiêkowych MPEG dla systemów unixowych.
Obs³uguje standart MPEG 1.0/2.0 warstwy 1, 2 oraz 3 (s³ynne "mp3"). Do
uzyskania pe³nej jako¶ci CD wymagany jest silny procesor (Pentium,
SPARCstation10, DEC Alpha lub podobny). Ni¿sz± jako¶æ (22 lub 11 kHz)
mo¿na uzyskaæ ju¿ na procesorach 486.

Wersja z wyj¶ciem na ESD.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%ifarch %{ix86}
%{__make} OPT_FLAGS="%{rpmcflags} -DINET6" linux
%else
%{__make} OPT_FLAGS="%{rpmcflags} -DINET6" linux-%{_target_cpu}
%endif

mv -f mpg123 mpg123.base

%{__make} clean
%ifarch %{ix86}
%{__make} OPT_FLAGS="%{rpmcflags} -DINET6" linux -esd
%else
%{__make} OPT_FLAGS="%{rpmcflags} -DINET6" linux-%{_target_cpu}-esd
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}.base	$RPM_BUILD_ROOT%{_bindir}/%{name}
install %{name}		$RPM_BUILD_ROOT%{_bindir}/%{name}-esd
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COPYING CHANGES JUKEBOX README BENCHMARKING README.remote TODO

%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-esd
