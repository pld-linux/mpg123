#
# TODO: check why SDL still doesn't work :/
#
# Conditional build:
%bcond_with	mmx	# use MMX to decode stream (won't run without MMX)
%bcond_without	esd	# disable esound supprot
%bcond_without	alsa	# disable alsa support
%bcond_without	jack	# disable jack support
%bcond_without	nas	# diasble nas support
%bcond_without	sdl	# disable sdl support
#
%ifarch pentium3 pentium4 athlon
%define		with_mmx	1
%endif
Summary:	MPEG audio player
Summary(es.UTF-8):   Ejecuta archivos MP3
Summary(pl.UTF-8):   Odtwarzacz plików audio MPEG
Summary(pt_BR.UTF-8):   Tocador de arquivos MP3
Summary(ru.UTF-8):   Проигрыватель MPEG аудиофайлов
Summary(uk.UTF-8):   Програвач MPEG аудіофайлів
Name:		mpg123
Version:	0.63
Release:	1
License:	LGPL, GPL (mpglib)
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
# Source0-md5:	781eb8a6c0726da55171cc18256e0756
Patch0:		%{name}-audio_sdl.patch
Patch1:		%{name}-audio_nas.patch
Patch2:		%{name}-am.patch
URL:		http://www.mpg123.de/
%{?with_sdl:BuildRequires:	SDL-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on i486 CPUs.

%description -l es.UTF-8
Ejecuta archivos MP3.

%description -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach i486.

%description -l pt_BR.UTF-8
O mpg123 é um tocador de áudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos "MP3").

%description -l ru.UTF-8
Mpg123 - это быстрый, свободный и переносимый проигрыватель MPEG
аудиофайлов. он поддерживает MPEG 1.0/2.0 уровней 1, 2 и 3 ("MP3"
файлы). Для получения качества звучания компакт-диска (44 kHz, 16 бит,
стерео) ноеобходим процессор Pentium. Монозвук или звук худшего
качества (22 kHz или 11 kHz) возможен и на процессорах класса i486.

%description -l uk.UTF-8
Mpg123 - це швидкий, вільний та переносимий програвач MPEG
аудіофайлів. Він підтримує MPEG 1.0/2.0 рівнів 1, 2 та 3 ("MP3"
файли). Для отримання якості звучання компакт-диску (44 kHz, 16 біт,
стерео) необхідний процесор Pentium. Монозвук чи звук гіршої якості
(22 kHz чи 11 kHz) можливий і на процесорах класу i486.

%package esd
Summary:	mpg123 for ESD
Summary(pl.UTF-8):   mpg123 dla ESD
Group:		Applications/Sound

%description esd
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ESD audio output.

%description esd -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach 486.

Wersja z wyjściem dźwięku przez ESD.

%package alsa
Summary:	mpg123 for ALSA
Summary(pl.UTF-8):   mpg123 dla ALSA
Group:		Applications/Sound

%description alsa
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for ALSA audio output.

%description alsa -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach 486.

Wersja z wyjściem dźwięku ALSA.

%package jack
Summary:	mpg123 for JACK
Summary(pl.UTF-8):   mpg123 dla JACK
Group:		Applications/Sound

%description jack
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for JACK audio output.

%description jack -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach 486.

Wersja z wyjściem dźwięku przez JACK.

%package nas
Summary:	mpg123 for NAS
Summary(pl.UTF-8):   mpg123 dla NAS
Group:		Applications/Sound

%description nas
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for NAS audio output.

%description nas -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach 486.

Wersja z wyjściem dźwięku przez NAS.

%package sdl
Summary:	mpg123 for SDL
Summary(pl.UTF-8):   mpg123 dla SDL
Group:		Applications/Sound

%description sdl
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on 486 CPUs.

Version for SDL output.

%description sdl -l pl.UTF-8
Mpg123 jest szybkim, darmowym (do celów niekomercyjnych) oraz
uniwersalnym dekoderem plików dźwiękowych MPEG dla systemów
uniksowych. Obsługuje standard MPEG 1.0/2.0 warstwy 1, 2 oraz 3
(słynne "MP3"). Do uzyskania pełnej jakości CD wymagany jest silny
procesor (Pentium, SPARCstation10, DEC Alpha lub podobny). Niższą
jakość (22 lub 11 kHz) można uzyskać już na procesorach 486.

Wersja z wyjściem dźwięku przez SDL.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-audio=oss \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123.base

%if %{with alsa}
%{__make} clean
%configure \
	%{?with_alsa:--with-audio=alsa} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-alsa
%endif

%if %{with esd}
%{__make} clean
%configure \
	%{?with_esd:--with-audio=esd} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-esd
%endif

%if %{with jack}
%{__make} clean
%configure \
	%{?with_jack:--with-audio=jack} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-jack
%endif

%if %{with nas}
%{__make} clean
%configure \
	%{?with_nas:--with-audio=nas} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-nas
%endif

%if %{with sdl}
%{__make} clean
%configure \
	%{?with_sdl:--with-audio=sdl} \
	%{?with_mmx:--with-cpu=mmx}
%{__make}
mv -f src/mpg123 src/mpg123-sdl
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/%{name}.base	$RPM_BUILD_ROOT%{_bindir}/%{name}

%if %{with alsa}
install src/%{name}-alsa		$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with esd}
install src/%{name}-esd		$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with jack}
install src/%{name}-jack	$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with nas}
install src/%{name}-nas		$RPM_BUILD_ROOT%{_bindir}/
%endif

%if %{with sdl}
install src/%{name}-sdl		$RPM_BUILD_ROOT%{_bindir}/
%endif

install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/BENCHMARKING doc/BUGS ChangeLog README doc/README.remote doc/TODO
%ifarch athlon
%doc doc/README.3DNOW
%endif
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-alsa
%endif

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-esd
%endif

%if %{with jack}
%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-jack
%endif

%if %{with nas}
%files nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-nas
%endif

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-sdl
%endif
