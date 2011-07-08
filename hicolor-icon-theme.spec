Summary: Basic requirement for icon themes
Name: hicolor-icon-theme
Version: 0.11
Release: 1.1%{?dist}
License: GPL+
Group: User Interface/Desktops
URL: http://icon-theme.freedesktop.org/wiki/HicolorTheme 
Source: http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires(post): coreutils
Requires(postun): coreutils

%description
Contains the basic directories and files needed for icon theme support.

%prep
%setup -q

# for some reason this file is executable in the tarball
chmod 0644 COPYING

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr install

touch $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_datadir}/icons/hicolor
%ghost %{_datadir}/icons/hicolor/icon-theme.cache

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.11-1.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009 Alexander Larsson <alexl@redhat.com> - 0.11-1
- Update to 0.11

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Matthias Clasen <mclasen@redhat.com> - 0.10-5
- Update URL
- Clean up scriptlets
- Include ChangeLog

* Sun Nov 18 2007 Matthias Clasen <mclasen@redhat.com> - 0.10-4
- Correct the license
- Include COPYING
- Add full source url

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 0.10-3
- Update the license field

* Fri Feb 23 2007 Matthias Clasen <mclasen@redhat.com> - 0.10-2
- Own the icon cache

* Thu Nov 23 2006 Alexander Larsson <alexl@redhat.com> - 0.10-1
- Update to 0.10

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9-2.1
- rebuild

* Mon Feb 27 2006 Ray Strode <rstrode@redhat.com> 0.9-2
- Remove Prereq on gtk.  Prereq's complicate things,
  and the gtk-update-icon-cache is already protected by
  [ -x  ... ]

* Thu Jan 12 2006 Alexander Larsson <alexl@redhat.com> 0.9-1
- Update to 0.9, fixes scalable icons picked before bitmap icons

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Florian La Roche <laroche@redhat.com>
- scripts need coreutils installed

* Tue Apr 19 2005 Matthias Clasen <mclasen@redhat.com> 0.8-2
- Silence %%post

* Thu Apr 14 2005 John (J5) Palmieri <johnp@redhat.com>
- Update to 0.8

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 0.7-2
- Update the GTK+ theme icon cache on (un)install

* Fri Feb  4 2005 Alexander Larsson <alexl@redhat.com> - 0.7-1
- Update to 0.7

* Wed Feb  2 2005 Alexander Larsson <alexl@redhat.com> - 0.6-1
- Update to 0.6

* Thu Jan 27 2005 Matthias Clasen <mclasen@redhat.com> - 0.5-1
- Update to 0.5

* Wed Sep 29 2004 GNOME <jrb@redhat.com> - 0.3-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb  4 2004 Alexander Larsson <alexl@redhat.com> 0.3-1
- update to 0.3

* Fri Jan 16 2004 Alexander Larsson <alexl@redhat.com> 0.2-1
- Initial build.


