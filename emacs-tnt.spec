%define rname 	tnt
%define name 	emacs-%{rname}
%define version 2.4
%define release  %mkrel 8

Summary: 	Emacs based AOL Instant Message Client
Name: 		%{name}
Version:	%{version}
Release: 	%{release}
Source0: 	%{rname}-%{version}.tar.bz2
Url:		http://tnt.sourceforge.net
License: 	GPL
Group: 		Editors
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Prefix: 	%{_prefix}
BuildRequires:  emacs-bin
BuildArch: noarch

%description
TNT is an Emacs client for AIM, AOL's free instant messaging service.
Using TNT, you can, from the comfort of your Emacs window, check
whether friends and coworkers are online, send them "instant
messages", and join them in multi-party private chat sessions.  Unlike
the official AIM clients, TNT is designed to be functional rather than
pretty, easy to use rather than easy to learn.  It doesn't have a
graphical user interface, fancy artwork, or other random fluff.
Instead, like other emacs extensions, it has a keyboard-driven,
text-based interface.  TNT is AIM for grownups ;-).

%prep
%setup -n %{rname}-%{version}

%build
emacs -batch --no-site-file --eval '(setq load-path (cons "." load-path))' -f batch-byte-compile *.el

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/tnt $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d
cp *.el *.elc $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d/tnt.el
(load "tnt")
EOF
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc README PROTOCOL TODO
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/emacs/site-lisp/*.elc
%{_sysconfdir}/emacs/site-start.d/tnt.el



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-8mdv2011.0
+ Revision: 618053
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.4-7mdv2010.0
+ Revision: 428588
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.4-6mdv2009.0
+ Revision: 244777
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.4-4mdv2008.1
+ Revision: 132767
- kill invalid packager tag
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import emacs-tnt


* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.4-4mdk
- rebuild for new emacs

* Sun Sep 07 2003 Pascal Terjan <CMoi@tuxfamily.org> 2.4-3mdk
- fix BuildRequires

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.4-2mdk
- rebuild for latest emacs

* Tue Sep 17 2002 Arnaud Desmons <adesmons@mandrakesoft.com> 2.4-1mdk
- first release

