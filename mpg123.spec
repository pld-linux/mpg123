#
# Conditional build:
%bcond_with	mmx	# use MMX to decode stream (won't run without MMX)
%bcond_without	esd	# don't build esound subpackage
#
Summary:	MPEG audio player
Summary(es):	Ejecuta archivos MP3
Summary(pl):	Odtwarzacz plikСw audio MPEG
Summary(pt_BR):	Tocador de arquivos MP3
Summary(ru):	Проигрыватель MPEG аудиофайлов
Summary(uk):	Програвач MPEG ауд╕офайл╕в
Name:		mpg123
Version:	0.59s
Release:	0.pre.6
Group:		Applications/Sound
License:	freely distributable for non-commercial use, GPL (mpglib)
Source0:	http://www.mpg123.de/mpg123/%{name}-pre%{version}.tar.gz
# Source0-md5: a63675b0ea7990d4a7d7e7e14f23a3e4
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-esd.patch
Patch2:		%{name}-audio_sun.patch
Patch3:		%{name}-security.patch
Patch4:		%{name}-id3v2-hack.patch
Patch5:		%{name}-http-overflow.patch
URL:		http://www.mpg123.de/
%{?with_esd:BuildRequires:	esound-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{ix86}
%ifarch athlon
%define		trgt	linux-3dnow
%else
%ifarch i586 i686
%define		trgt	linux%{?with_mmx:-mmx}
%else
%define		trgt	linux-i486
%endif
%endif
%else
%define		trgt	linux-%{_target_cpu}
%endif

%define		specflags	-fomit-frame-pointer

%description
Mpg123 is a fast, free(for non-commercial use) and portable MPEG audio
player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3 (those
famous "mp3" files). For full CD quality playback (44 kHz, 16 bit,
stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on i486 CPUs.

%description -l es
Ejecuta archivos MP3.

%description -l pl
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw unixowych.
ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3 (sЁynne "mp3"). Do
uzyskania peЁnej jako╤ci CD wymagany jest silny procesor (Pentium,
SPARCstation10, DEC Alpha lub podobny). Ni©sz╠ jako╤Ф (22 lub 11 kHz)
mo©na uzyskaФ ju© na procesorach i486.

%description -l pt_BR
O mpg123 И um tocador de Аudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos .mp3).

%description -l ru
Mpg123 - это быстрый, свободный и переносимый проигрыватель MPEG
аудиофайлов. он поддерживает MPEG 1.0/2.0 уровней 1, 2 и 3 ("mp3"
файлы). Для получения качества звучания компакт-диска (44 kHz, 16 бит,
стерео) ноеобходим процессор Pentium. Монозвук или звук худшего
качества (22 kHz или 11 kHz) возможен и на процессорах класса i486.

%description -l uk
Mpg123 - це швидкий, в╕льний та переносимий програвач MPEG
ауд╕офайл╕в. В╕н п╕дтриму╓ MPEG 1.0/2.0 р╕вн╕в 1, 2 та 3 ("mp3"
файли). Для отримання якост╕ звучання компакт-диску (44 kHz, 16 б╕т,
стерео) необх╕дний процесор Pentium. Монозвук чи звук г╕ршо╖ якост╕
(22 kHz чи 11 kHz) можливий ╕ на процесорах класу i486.

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
Mpg123 jest szybkim, darmowym (do celСw niekomercyjnych) oraz
uniwersalnym dekoderem plikСw d╪wiЙkowych MPEG dla systemСw unixowych.
ObsЁuguje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3 (sЁynne "mp3"). Do
uzyskania peЁnej jako╤ci CD wymagany jest silny procesor (Pentium,
SPARCstation10, DEC Alpha lub podobny). Ni©sz╠ jako╤Ф (22 lub 11 kHz)
mo©na uzyskaФ ju© na procesorach 486.

Wersja z wyj╤ciem na ESD.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__make} %{trgt} \
	OPT_FLAGS="%{rpmcflags} -DINET6"

mv -f mpg123 mpg123.base
%if %{with esd}
%{__make} clean
%{__make} %{trgt}-esd \
	OPT_FLAGS="%{rpmcflags} -DINET6"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}.base	$RPM_BUILD_ROOT%{_bindir}/%{name}
%if %{with esd}
install %{name}		$RPM_BUILD_ROOT%{_bindir}/%{name}-esd
%endif
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARKING BUGS CHANGES COPYING JUKEBOX README README.remote TODO
%ifarch athlon
%doc README.3DNOW
%endif
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-esd
%endif
