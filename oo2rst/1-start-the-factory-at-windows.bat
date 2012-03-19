: mb, 2012-03-14, 2012-03-18

: 2012-03-18  now complete

:set path="d:\InstalledPrograms\LibreOffice 3.4\program\";%path%



: Step 1: Make OpenOffice create an HTML version
 
:soffice  --headless  -convert-to html  -outdir .\doc_core_api\doc_core_api\doc\img                        doc_core_api\doc_core_api\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir .\doc_core_cgl\doc_core_cgl\doc\img                        doc_core_cgl\doc_core_cgl\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_cgl\doc_core_cgl_fr\doc\img                       doc_core_cgl\doc_core_cgl_fr\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_cgl\doc_core_cgl_ru\doc\img                       doc_core_cgl\doc_core_cgl_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_inside\doc_core_inside\doc\img                    doc_core_inside\doc_core_inside\doc\doc_core_inside.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_services\doc_core_services\doc\img                doc_core_services\doc_core_services\doc\doc_core_services.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_skinning\doc_core_skinning\doc\img                doc_core_skinning\doc_core_skinning\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tca\doc_core_tca\doc\img                          doc_core_tca\doc_core_tca\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_ts\doc_core_ts\doc\img                            doc_core_ts\doc_core_ts\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tsconfig\doc_core_tsconfig\doc\img                doc_core_tsconfig\doc_core_tsconfig\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tsconfig\doc_core_tsconfig_fr\doc\img             doc_core_tsconfig\doc_core_tsconfig_fr\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tsconfig\doc_core_tsconfig_ru\doc\img             doc_core_tsconfig\doc_core_tsconfig_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tsref\doc_core_tsref\doc\img                      doc_core_tsref\doc_core_tsref\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tsref\doc_core_tsref_fr\doc\img                   doc_core_tsref\doc_core_tsref_fr\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_core_tsref\doc_core_tsref_ru\doc\img                   doc_core_tsref\doc_core_tsref_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_admin\doc_guide_admin\doc\img                    doc_guide_admin\doc_guide_admin\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install\doc\img                doc_guide_install\doc_guide_install\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install\doc\img                doc_guide_install\doc_guide_install\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_da\doc\img             doc_guide_install\doc_guide_install_da\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_da\doc\img             doc_guide_install\doc_guide_install_da\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_fr\doc\img             doc_guide_install\doc_guide_install_fr\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_fr\doc\img             doc_guide_install\doc_guide_install_fr\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_ja\doc\img             doc_guide_install\doc_guide_install_ja\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_ja\doc\img             doc_guide_install\doc_guide_install_ja\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_ru\doc\img             doc_guide_install\doc_guide_install_ru\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_guide_install\doc_guide_install_ru\doc\img             doc_guide_install\doc_guide_install_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_l10n\doc_guide_l10n\doc\img                      doc_guide_l10n\doc_guide_l10n\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_l10n\doc_guide_l10n_ru\doc\img                   doc_guide_l10n\doc_guide_l10n_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_guide_security\doc_guide_security\doc\img              doc_guide_security\doc_guide_security\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_indexed_search\doc\img                                 doc_indexed_search\doc\doc_indexed_search.sxw
:soffice  --headless  -convert-to html  -outdir doc_template\doc\img                                       doc_template\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_editors\doc_tut_editors_basicreference\doc\img     doc_tut_editors\doc_tut_editors\doc\basicreference.odt
:soffice  --headless  -convert-to html  -outdir doc_tut_editors\doc_tut_editors_manual\doc\img             doc_tut_editors\doc_tut_editors\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_editors\doc_tut_editors_partsnotinmanual\doc\img   doc_tut_editors\doc_tut_editors\doc\partsnotinmanual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart\doc\img              doc_tut_quickstart\doc_tut_quickstart\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_da\doc\img           doc_tut_quickstart\doc_tut_quickstart_da\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_de\doc\img           doc_tut_quickstart\doc_tut_quickstart_de\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_fr\doc\img           doc_tut_quickstart\doc_tut_quickstart_fr\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_ja\doc\img           doc_tut_quickstart\doc_tut_quickstart_ja\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_nl\doc\img           doc_tut_quickstart\doc_tut_quickstart_nl\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_ro\doc\img           doc_tut_quickstart\doc_tut_quickstart_ro\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_quickstart\doc_tut_quickstart_ru\doc\img           doc_tut_quickstart\doc_tut_quickstart_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45\doc\img                          doc_tut_ts45\doc_tut_ts45\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45\doc\img                          doc_tut_ts45\doc_tut_ts45\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_da\doc\img                       doc_tut_ts45\doc_tut_ts45_da\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_da\doc\img                       doc_tut_ts45\doc_tut_ts45_da\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_de\doc\img                       doc_tut_ts45\doc_tut_ts45_de\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_de\doc\img                       doc_tut_ts45\doc_tut_ts45_de\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_it\doc\img                       doc_tut_ts45\doc_tut_ts45_it\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_it\doc\img                       doc_tut_ts45\doc_tut_ts45_it\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_ja\doc\img                       doc_tut_ts45\doc_tut_ts45_ja\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_ja\doc\img                       doc_tut_ts45\doc_tut_ts45_ja\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_nl\doc\img                       doc_tut_ts45\doc_tut_ts45_nl\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_nl\doc\img                       doc_tut_ts45\doc_tut_ts45_nl\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_ru\doc\img                       doc_tut_ts45\doc_tut_ts45_ru\doc\manual.odt
:rem      --headless  -convert-to html  -outdir doc_tut_ts45\doc_tut_ts45_ru\doc\img                       doc_tut_ts45\doc_tut_ts45_ru\doc\manual.sxw
:soffice  --headless  -convert-to html  -outdir official_template\DocBook\docs\img                         official_template\DocBook\docs\manual2.sxw
:soffice  --headless  -convert-to html  -outdir official_template\OpenOffice\img                           official_template\OpenOffice\official_documentation_template.ott



: Step 2: Tweak the *.html files

:tweak_oohtml  -v  doc_core_api\doc_core_api\doc\img\manual.html                                   doc_core_api\doc_core_api\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_cgl\doc_core_cgl\doc\img\manual.html                                   doc_core_cgl\doc_core_cgl\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_cgl\doc_core_cgl_fr\doc\img\manual.html                                doc_core_cgl\doc_core_cgl_fr\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_cgl\doc_core_cgl_ru\doc\img\manual.html                                doc_core_cgl\doc_core_cgl_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_inside\doc_core_inside\doc\img\doc_core_inside.html                    doc_core_inside\doc_core_inside\doc\img\doc_core_inside-tweaked.html
:tweak_oohtml  -v  doc_core_services\doc_core_services\doc\img\doc_core_services.html              doc_core_services\doc_core_services\doc\img\doc_core_services-tweaked.html
:tweak_oohtml  -v  doc_core_skinning\doc_core_skinning\doc\img\manual.html                         doc_core_skinning\doc_core_skinning\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tca\doc_core_tca\doc\img\manual.html                                   doc_core_tca\doc_core_tca\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_ts\doc_core_ts\doc\img\manual.html                                     doc_core_ts\doc_core_ts\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tsconfig\doc_core_tsconfig\doc\img\manual.html                         doc_core_tsconfig\doc_core_tsconfig\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tsconfig\doc_core_tsconfig_fr\doc\img\manual.html                      doc_core_tsconfig\doc_core_tsconfig_fr\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tsconfig\doc_core_tsconfig_ru\doc\img\manual.html                      doc_core_tsconfig\doc_core_tsconfig_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tsref\doc_core_tsref\doc\img\manual.html                               doc_core_tsref\doc_core_tsref\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tsref\doc_core_tsref_fr\doc\img\manual.html                            doc_core_tsref\doc_core_tsref_fr\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_core_tsref\doc_core_tsref_ru\doc\img\manual.html                            doc_core_tsref\doc_core_tsref_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_admin\doc_guide_admin\doc\img\manual.html                             doc_guide_admin\doc_guide_admin\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_install\doc_guide_install\doc\img\manual.html                         doc_guide_install\doc_guide_install\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_install\doc_guide_install_da\doc\img\manual.html                      doc_guide_install\doc_guide_install_da\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_install\doc_guide_install_fr\doc\img\manual.html                      doc_guide_install\doc_guide_install_fr\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_install\doc_guide_install_ja\doc\img\manual.html                      doc_guide_install\doc_guide_install_ja\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_install\doc_guide_install_ru\doc\img\manual.html                      doc_guide_install\doc_guide_install_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_l10n\doc_guide_l10n\doc\img\manual.html                               doc_guide_l10n\doc_guide_l10n\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_l10n\doc_guide_l10n_ru\doc\img\manual.html                            doc_guide_l10n\doc_guide_l10n_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_guide_security\doc_guide_security\doc\img\manual.html                       doc_guide_security\doc_guide_security\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_indexed_search\doc\img\doc_indexed_search.html                              doc_indexed_search\doc\img\doc_indexed_search-tweaked.html
:tweak_oohtml  -v  doc_template\doc\img\manual.html                                                doc_template\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_editors\doc_tut_editors_basicreference\doc\img\basicreference.html      doc_tut_editors\doc_tut_editors_basicreference\doc\img\basicreference-tweaked.html
:tweak_oohtml  -v  doc_tut_editors\doc_tut_editors_manual\doc\img\manual.html                      doc_tut_editors\doc_tut_editors_manual\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_editors\doc_tut_editors_partsnotinmanual\doc\img\partsnotinmanual.html  doc_tut_editors\doc_tut_editors_partsnotinmanual\doc\img\partsnotinmanual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart\doc\img\manual.html                       doc_tut_quickstart\doc_tut_quickstart\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_da\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_da\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_de\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_de\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_fr\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_fr\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_ja\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_ja\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_nl\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_nl\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_ro\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_ro\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_quickstart\doc_tut_quickstart_ru\doc\img\manual.html                    doc_tut_quickstart\doc_tut_quickstart_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45\doc\img\manual.html                                   doc_tut_ts45\doc_tut_ts45\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45_da\doc\img\manual.html                                doc_tut_ts45\doc_tut_ts45_da\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45_de\doc\img\manual.html                                doc_tut_ts45\doc_tut_ts45_de\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45_it\doc\img\manual.html                                doc_tut_ts45\doc_tut_ts45_it\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45_ja\doc\img\manual.html                                doc_tut_ts45\doc_tut_ts45_ja\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45_nl\doc\img\manual.html                                doc_tut_ts45\doc_tut_ts45_nl\doc\img\manual-tweaked.html
:tweak_oohtml  -v  doc_tut_ts45\doc_tut_ts45_ru\doc\img\manual.html                                doc_tut_ts45\doc_tut_ts45_ru\doc\img\manual-tweaked.html
:tweak_oohtml  -v  official_template\DocBook\docs\img\manual2.html                                 official_template\DocBook\docs\img\manual2-tweaked.html
:tweak_oohtml  -v  official_template\OpenOffice\img\official_documentation_template.html           official_template\OpenOffice\img\official_documentation_template-tweaked.html



: Step 3: From *-tweaked.html to *.rst

:ooxhtml2rst    doc_core_api\doc_core_api\doc\img\manual-tweaked.html                                   doc_core_api\doc_core_api\doc\img\manual.rst
:ooxhtml2rst    doc_core_cgl\doc_core_cgl\doc\img\manual-tweaked.html                                   doc_core_cgl\doc_core_cgl\doc\img\manual.rst
:ooxhtml2rst    doc_core_cgl\doc_core_cgl_fr\doc\img\manual-tweaked.html                                doc_core_cgl\doc_core_cgl_fr\doc\img\manual.rst
:ooxhtml2rst    doc_core_cgl\doc_core_cgl_ru\doc\img\manual-tweaked.html                                doc_core_cgl\doc_core_cgl_ru\doc\img\manual.rst
:ooxhtml2rst    doc_core_inside\doc_core_inside\doc\img\doc_core_inside-tweaked.html                    doc_core_inside\doc_core_inside\doc\img\doc_core_inside.rst
:ooxhtml2rst    doc_core_services\doc_core_services\doc\img\doc_core_services-tweaked.html              doc_core_services\doc_core_services\doc\img\doc_core_services.rst
:ooxhtml2rst    doc_core_skinning\doc_core_skinning\doc\img\manual-tweaked.html                         doc_core_skinning\doc_core_skinning\doc\img\manual.rst
:ooxhtml2rst    doc_core_tca\doc_core_tca\doc\img\manual-tweaked.html                                   doc_core_tca\doc_core_tca\doc\img\manual.rst
:ooxhtml2rst    doc_core_ts\doc_core_ts\doc\img\manual-tweaked.html                                     doc_core_ts\doc_core_ts\doc\img\manual.rst
:ooxhtml2rst    doc_core_tsconfig\doc_core_tsconfig\doc\img\manual-tweaked.html                         doc_core_tsconfig\doc_core_tsconfig\doc\img\manual.rst
:ooxhtml2rst    doc_core_tsconfig\doc_core_tsconfig_fr\doc\img\manual-tweaked.html                      doc_core_tsconfig\doc_core_tsconfig_fr\doc\img\manual.rst
:ooxhtml2rst    doc_core_tsconfig\doc_core_tsconfig_ru\doc\img\manual-tweaked.html                      doc_core_tsconfig\doc_core_tsconfig_ru\doc\img\manual.rst
:ooxhtml2rst    doc_core_tsref\doc_core_tsref\doc\img\manual-tweaked.html                               doc_core_tsref\doc_core_tsref\doc\img\manual.rst
:ooxhtml2rst    doc_core_tsref\doc_core_tsref_fr\doc\img\manual-tweaked.html                            doc_core_tsref\doc_core_tsref_fr\doc\img\manual.rst
:ooxhtml2rst    doc_core_tsref\doc_core_tsref_ru\doc\img\manual-tweaked.html                            doc_core_tsref\doc_core_tsref_ru\doc\img\manual.rst
:ooxhtml2rst    doc_guide_admin\doc_guide_admin\doc\img\manual-tweaked.html                             doc_guide_admin\doc_guide_admin\doc\img\manual.rst
:ooxhtml2rst    doc_guide_install\doc_guide_install\doc\img\manual-tweaked.html                         doc_guide_install\doc_guide_install\doc\img\manual.rst
:ooxhtml2rst    doc_guide_install\doc_guide_install_da\doc\img\manual-tweaked.html                      doc_guide_install\doc_guide_install_da\doc\img\manual.rst
:ooxhtml2rst    doc_guide_install\doc_guide_install_fr\doc\img\manual-tweaked.html                      doc_guide_install\doc_guide_install_fr\doc\img\manual.rst
:ooxhtml2rst    doc_guide_install\doc_guide_install_ja\doc\img\manual-tweaked.html                      doc_guide_install\doc_guide_install_ja\doc\img\manual.rst
:ooxhtml2rst    doc_guide_install\doc_guide_install_ru\doc\img\manual-tweaked.html                      doc_guide_install\doc_guide_install_ru\doc\img\manual.rst
:ooxhtml2rst    doc_guide_l10n\doc_guide_l10n\doc\img\manual-tweaked.html                               doc_guide_l10n\doc_guide_l10n\doc\img\manual.rst
:ooxhtml2rst    doc_guide_l10n\doc_guide_l10n_ru\doc\img\manual-tweaked.html                            doc_guide_l10n\doc_guide_l10n_ru\doc\img\manual.rst
:ooxhtml2rst    doc_guide_security\doc_guide_security\doc\img\manual-tweaked.html                       doc_guide_security\doc_guide_security\doc\img\manual.rst
:ooxhtml2rst    doc_indexed_search\doc\img\doc_indexed_search-tweaked.html                              doc_indexed_search\doc\img\doc_indexed_search.rst
:ooxhtml2rst    doc_template\doc\img\manual-tweaked.html                                                doc_template\doc\img\manual.rst
:ooxhtml2rst    doc_tut_editors\doc_tut_editors_basicreference\doc\img\basicreference-tweaked.html      doc_tut_editors\doc_tut_editors_basicreference\doc\img\basicreference-tweaked.rst
:ooxhtml2rst    doc_tut_editors\doc_tut_editors_manual\doc\img\manual-tweaked.html                      doc_tut_editors\doc_tut_editors_manual\doc\img\manual-tweaked.rst       
:ooxhtml2rst    doc_tut_editors\doc_tut_editors_partsnotinmanual\doc\img\partsnotinmanual-tweaked.html  doc_tut_editors\doc_tut_editors_partsnotinmanual\doc\img\partsnotinmanual-tweaked.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart\doc\img\manual-tweaked.html                       doc_tut_quickstart\doc_tut_quickstart\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_da\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_da\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_de\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_de\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_fr\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_fr\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_ja\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_ja\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_nl\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_nl\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_ro\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_ro\doc\img\manual.rst
:ooxhtml2rst    doc_tut_quickstart\doc_tut_quickstart_ru\doc\img\manual-tweaked.html                    doc_tut_quickstart\doc_tut_quickstart_ru\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45\doc\img\manual-tweaked.html                                   doc_tut_ts45\doc_tut_ts45\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45_da\doc\img\manual-tweaked.html                                doc_tut_ts45\doc_tut_ts45_da\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45_de\doc\img\manual-tweaked.html                                doc_tut_ts45\doc_tut_ts45_de\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45_it\doc\img\manual-tweaked.html                                doc_tut_ts45\doc_tut_ts45_it\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45_ja\doc\img\manual-tweaked.html                                doc_tut_ts45\doc_tut_ts45_ja\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45_nl\doc\img\manual-tweaked.html                                doc_tut_ts45\doc_tut_ts45_nl\doc\img\manual.rst
:ooxhtml2rst    doc_tut_ts45\doc_tut_ts45_ru\doc\img\manual-tweaked.html                                doc_tut_ts45\doc_tut_ts45_ru\doc\img\manual.rst
:ooxhtml2rst    official_template\DocBook\docs\img\manual2-tweaked.html                                 official_template\DocBook\docs\img\manual2.rst
:ooxhtml2rst    official_template\OpenOffice\img\official_documentation_template-tweaked.html           official_template\OpenOffice\img\official_documentation_template.rst



: Step 4: From doc/img/*.rst to doc/source/ Sphinx structure

:the_little_rest_slicer   doc_core_api\doc_core_api\doc\img\manual.rst
:the_little_rest_slicer   doc_core_cgl\doc_core_cgl\doc\img\manual.rst
:the_little_rest_slicer   doc_core_cgl\doc_core_cgl_fr\doc\img\manual.rst
:the_little_rest_slicer   doc_core_cgl\doc_core_cgl_ru\doc\img\manual.rst
:the_little_rest_slicer   doc_core_inside\doc_core_inside\doc\img\doc_core_inside.rst
:the_little_rest_slicer   doc_core_services\doc_core_services\doc\img\doc_core_services.rst
:the_little_rest_slicer   doc_core_skinning\doc_core_skinning\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tca\doc_core_tca\doc\img\manual.rst
:the_little_rest_slicer   doc_core_ts\doc_core_ts\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tsconfig\doc_core_tsconfig\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tsconfig\doc_core_tsconfig_fr\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tsconfig\doc_core_tsconfig_ru\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tsref\doc_core_tsref\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tsref\doc_core_tsref_fr\doc\img\manual.rst
:the_little_rest_slicer   doc_core_tsref\doc_core_tsref_ru\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_admin\doc_guide_admin\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_install\doc_guide_install\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_install\doc_guide_install_da\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_install\doc_guide_install_fr\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_install\doc_guide_install_ja\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_install\doc_guide_install_ru\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_l10n\doc_guide_l10n\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_l10n\doc_guide_l10n_ru\doc\img\manual.rst
:the_little_rest_slicer   doc_guide_security\doc_guide_security\doc\img\manual.rst
:the_little_rest_slicer   doc_indexed_search\doc\img\doc_indexed_search.rst
:the_little_rest_slicer   doc_template\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_editors\doc_tut_editors_basicreference\doc\img\basicreference-tweaked.rst
:the_little_rest_slicer   doc_tut_editors\doc_tut_editors_manual\doc\img\manual-tweaked.rst       
:the_little_rest_slicer   doc_tut_editors\doc_tut_editors_partsnotinmanual\doc\img\partsnotinmanual-tweaked.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_da\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_de\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_fr\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_ja\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_nl\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_ro\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_quickstart\doc_tut_quickstart_ru\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45_da\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45_de\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45_it\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45_ja\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45_nl\doc\img\manual.rst
:the_little_rest_slicer   doc_tut_ts45\doc_tut_ts45_ru\doc\img\manual.rst
:the_little_rest_slicer   official_template\DocBook\docs\img\manual2.rst
:the_little_rest_slicer   official_template\OpenOffice\img\official_documentation_template.rst



: Step 5: Manually edit the destination builddir for Sphinx in */Makefile

