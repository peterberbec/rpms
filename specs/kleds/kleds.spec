# $Id$
# Authority: dries

# Screenshot: http://www.hansmatzen.de/pics/kleds_ss01.png
# ScreenshotURL: http://www.hansmatzen.de/english/kleds.html#screenshots

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Shows the status of the keyboard indicator LEDs in the KDE panel
Name: kleds
Version: 0.8.0
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://www.hansmatzen.de/english/kleds.html

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://www.hansmatzen.de/software/kleds/kleds-%{version}.tar.bz2
BuildRequires: gcc, gcc-c++, qt-devel, kdelibs-devel
BuildRequires: zlib-devel, libart_lgpl-devel, make, arts-devel, gettext
BuildRequires: libpng-devel, libjpeg-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
KLeds is a little program for the KDE Desktop Environment. It shows 
up in the KDE Panel and displays the current state of the keyboard 
indicator LED's (NumLock, ScrollLock and CapsLock).

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/kleds
%{_bindir}/kledsd

%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.8.0-2
- Spec file cleanup, added %%find_lang.

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.8.0-2
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.8.0-1
- first packaging for Fedora Core 1

