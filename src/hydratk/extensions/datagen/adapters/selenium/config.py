# -*- coding: utf-8 -*-
"""Configuration for Selenium adapter

.. module:: datagen.adapters.selenium.config
   :platform: Unix
   :synopsis: Configuration for Selenium adapter
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

tmpl_scenario = """Test-Scenario-1:
  Id: ts_1
  Path: path to file
  Name: {title}
  Desc: description
  Author: author
  Version: 0.1
  
  Pre-Req: | 
    {pre_req}
  
  {cases}  
"""

tmpl_case = """Test-Case-{idx}:
    Id: tc_{idx}
    Name: {title}
    Desc: description
    
    {conditions}
"""

tmpl_condition = """Test-Condition-{idx}: 
      Id: tco_{idx}
      Name: {title}
      Desc: description
  
      Test: |
        {test}
  
      Validate: |
        {validate}
        
"""

tmpl_pre_req = """from hydratk.lib.bridge.selen import SeleniumBridge
    from hydratk.lib.data.share import my
    from time import sleep"""

tmpl_validate = """this.test_result = str(res)
        """

mapping = {
    'addLocationStrategy': 'cmd_dummy',
    'addLocationStrategyAndWait': 'cmd_dummy',
    'addScript': 'cmd_dummy',
    'addScriptAndWait': 'cmd_dummy',
    'addSelection': 'cmd_dummy',
    'addSelectionAndWait': 'cmd_dummy',
    'allowNativeXpath': 'cmd_dummy',
    'allowNativeXpathAndWait': 'cmd_dummy',
    'altKeyDown': 'cmd_dummy',
    'altKeyDownAndWait': 'cmd_dummy',
    'altKeyUp': 'cmd_dummy',
    'altKeyUpAndWait': 'cmd_dummy',
    'answerOnNextPrompt': 'cmd_dummy',
    'assertAlert': 'cmd_alert',
    'assertAlertNotPresent': 'cmd_alert',
    'assertAlertPresent': 'cmd_alert',
    'assertAllButtons': 'cmd_dummy',
    'assertAllFields': 'cmd_dummy',
    'assertAllLinks': 'cmd_dummy',
    'assertAllWindowIds': 'cmd_dummy',
    'assertAllWindowNames': 'cmd_dummy',
    'assertAllWindowTitles': 'cmd_dummy',
    'assertAttribute': 'cmd_verify',
    'assertAttributeFromAllWindows': 'cmd_dummy',
    'assertBodyText': 'cmd_verify',
    'assertChecked': 'cmd_verify',
    'assertConfirmation': 'cmd_alert',
    'assertConfirmationNotPresent': 'cmd_alert',
    'assertConfirmationPresent': 'cmd_alert',
    'assertCookie': 'cmd_dummy',
    'assertCookieByName': 'cmd_dummy',
    'assertCookieNotPresent': 'cmd_dummy',
    'assertCookiePresent': 'cmd_dummy',
    'assertCursorPosition': 'cmd_dummy',
    'assertEditable': 'cmd_dummy',
    'assertElementHeight': 'cmd_dummy',
    'assertElementIndex': 'cmd_dummy',
    'assertElementNotPresent': 'cmd_verify',
    'assertElementPositionLeft': 'cmd_dummy',
    'assertElementPositionTop': 'cmd_dummy',
    'assertElementPresent': 'cmd_verify',
    'assertElementWidth': 'cmd_dummy',
    'assertEval': 'cmd_dummy',
    'assertExpression': 'cmd_dummy',
    'assertHtmlSource': 'cmd_dummy',
    'assertLocation': 'cmd_verify',
    'assertMouseSpeed': 'cmd_dummy',
    'assertNotAlert': 'cmd_alert',
    'assertNotAllButtons': 'cmd_dummy',
    'assertNotAllFields': 'cmd_dummy',
    'assertNotAllLinks': 'cmd_dummy',
    'assertNotAllWindowIds': 'cmd_dummy',
    'assertNotAllWindowNames': 'cmd_dummy',
    'assertNotAllWindowTitles': 'cmd_dummy',
    'assertNotAttribute': 'cmd_verify',
    'assertNotAttributeFromAllWindows': 'cmd_dummy',
    'assertNotBodyText': 'cmd_verify',
    'assertNotChecked': 'cmd_verify',
    'assertNotConfirmation': 'cmd_alert',
    'assertNotCookie': 'cmd_dummy',
    'assertNotCookieByName': 'cmd_dummy',
    'assertNotCursorPosition': 'cmd_dummy',
    'assertNotEditable': 'cmd_dummy',
    'assertNotElementHeight': 'cmd_dummy',
    'assertNotElementIndex': 'cmd_dummy',
    'assertNotElementPositionLeft': 'cmd_dummy',
    'assertNotElementPositionTop': 'cmd_dummy',
    'assertNotElementWidth': 'cmd_dummy',
    'assertNotEval': 'cmd_dummy',
    'assertNotExpression': 'cmd_dummy',
    'assertNotHtmlSource': 'cmd_dummy',
    'assertNotLocation': 'cmd_verify',
    'assertNotMouseSpeed': 'cmd_dummy',
    'assertNotOrdered': 'cmd_dummy',
    'assertNotPrompt': 'cmd_dummy',
    'assertNotSelectOptions': 'cmd_dummy',
    'assertNotSelectedId': 'cmd_dummy',
    'assertNotSelectedIds': 'cmd_dummy',
    'assertNotSelectedIndex': 'cmd_dummy',
    'assertNotSelectedIndexes': 'cmd_dummy',
    'assertNotSelectedLabel': 'cmd_dummy',
    'assertNotSelectedLabels': 'cmd_dummy',
    'assertNotSelectedValue': 'cmd_dummy',
    'assertNotSelectedValues': 'cmd_dummy',
    'assertNotSomethingSelected': 'cmd_dummy',
    'assertNotSpeed': 'cmd_dummy',
    'assertNotTable': 'cmd_dummy',
    'assertNotText': 'cmd_verify',
    'assertNotTitle': 'cmd_verify',
    'assertNotValue': 'cmd_verify',
    'assertNotVisible': 'cmd_verify',
    'assertNotWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'assertNotWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'assertNotXpathCount': 'cmd_verify',
    'assertOrdered': 'cmd_dummy',
    'assertPrompt': 'cmd_dummy',
    'assertPromptNotPresent': 'cmd_dummy',
    'assertPromptPresent': 'cmd_dummy',
    'assertSelectOptions': 'cmd_dummy',
    'assertSelectedId': 'cmd_dummy',
    'assertSelectedIds': 'cmd_dummy',
    'assertSelectedIndex': 'cmd_dummy',
    'assertSelectedIndexes': 'cmd_dummy',
    'assertSelectedLabel': 'cmd_dummy',
    'assertSelectedLabels': 'cmd_dummy',
    'assertSelectedValue': 'cmd_dummy',
    'assertSelectedValues': 'cmd_dummy',
    'assertSomethingSelected': 'cmd_dummy',
    'assertSpeed': 'cmd_dummy',
    'assertTable': 'cmd_dummy',
    'assertText': 'cmd_verify',
    'assertTextNotPresent': 'cmd_dummy',
    'assertTextPresent': 'cmd_dummy',
    'assertTitle': 'cmd_verify',
    'assertValue': 'cmd_verify',
    'assertVisible': 'cmd_verify',
    'assertWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'assertWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'assertXpathCount': 'cmd_verify',
    'assignId': 'cmd_dummy',
    'assignIdAndWait': 'cmd_dummy',
    'break': 'cmd_dummy',
    'captureEntirePageScreenshot': 'cmd_dummy',
    'captureEntirePageScreenshotAndWait': 'cmd_dummy',
    'check': 'cmd_set',
    'checkAndWait': 'cmd_set',
    'chooseCancelOnNextConfirmation': 'cmd_alert',
    'chooseOkOnNextConfirmation': 'cmd_alert',
    'chooseOkOnNextConfirmationAndWait': 'cmd_alert',
    'click': 'cmd_set',
    'clickAndWait': 'cmd_set',
    'clickAt': 'cmd_dummy',
    'clickAtAndWait': 'cmd_dummy',
    'close': 'cmd_close',
    'contextMenu': 'cmd_dummy',
    'contextMenuAndWait': 'cmd_dummy',
    'contextMenuAt': 'cmd_dummy',
    'contextMenuAtAndWait': 'cmd_dummy',
    'controlKeyDown': 'cmd_dummy',
    'controlKeyDownAndWait': 'cmd_dummy',
    'controlKeyUp': 'cmd_dummy',
    'controlKeyUpAndWait': 'cmd_dummy',
    'createCookie': 'cmd_dummy',
    'createCookieAndWait': 'cmd_dummy',
    'deleteAllVisibleCookies': 'cmd_dummy',
    'deleteAllVisibleCookiesAndWait': 'cmd_dummy',
    'deleteCookie': 'cmd_dummy',
    'deleteCookieAndWait': 'cmd_dummy',
    'deselectPopUp': 'cmd_dummy',
    'deselectPopUpAndWait': 'cmd_dummy',
    'doubleClick': 'cmd_dummy',
    'doubleClickAndWait': 'cmd_dummy',
    'doubleClickAt': 'cmd_dummy',
    'doubleClickAtAndWait': 'cmd_dummy',
    'dragAndDrop': 'cmd_dummy',
    'dragAndDropAndWait': 'cmd_dummy',
    'dragAndDropToObject': 'cmd_dummy',
    'dragAndDropToObjectAndWait': 'cmd_dummy',
    'dragdrop': 'cmd_dummy',
    'dragdropAndWait': 'cmd_dummy',
    'echo': 'cmd_echo',
    'fireEvent': 'cmd_dummy',
    'fireEventAndWait': 'cmd_dummy',
    'focus': 'cmd_dummy',
    'focusAndWait': 'cmd_dummy',
    'goBack': 'cmd_go_back',
    'goBackAndWait': 'cmd_go_back',
    'highlight': 'cmd_dummy',
    'highlightAndWait': 'cmd_dummy',
    'ignoreAttributesWithoutValue': 'cmd_dummy',
    'ignoreAttributesWithoutValueAndWait': 'cmd_dummy',
    'keyDown': 'cmd_dummy',
    'keyDownAndWait': 'cmd_dummy',
    'keyPress': 'cmd_dummy',
    'keyPressAndWait': 'cmd_dummy',
    'keyUp': 'cmd_dummy',
    'keyUpAndWait': 'cmd_dummy',
    'metaKeyDown': 'cmd_dummy',
    'metaKeyDownAndWait': 'cmd_dummy',
    'metaKeyUp': 'cmd_dummy',
    'metaKeyUpAndWait': 'cmd_dummy',
    'mouseDown': 'cmd_dummy',
    'mouseDownAndWait': 'cmd_dummy',
    'mouseDownAt': 'cmd_dummy',
    'mouseDownAtAndWait': 'cmd_dummy',
    'mouseDownRight': 'cmd_dummy',
    'mouseDownRightAndWait': 'cmd_dummy',
    'mouseDownRightAt': 'cmd_dummy',
    'mouseDownRightAtAndWait': 'cmd_dummy',
    'mouseMove': 'cmd_dummy',
    'mouseMoveAndWait': 'cmd_dummy',
    'mouseMoveAt': 'cmd_dummy',
    'mouseMoveAtAndWait': 'cmd_dummy',
    'mouseOut': 'cmd_dummy',
    'mouseOutAndWait': 'cmd_dummy',
    'mouseOver': 'cmd_dummy',
    'mouseOverAndWait': 'cmd_dummy',
    'mouseUp': 'cmd_dummy',
    'mouseUpAndWait': 'cmd_dummy',
    'mouseUpAt': 'cmd_dummy',
    'mouseUpAtAndWait': 'cmd_dummy',
    'mouseUpRight': 'cmd_dummy',
    'mouseUpRightAndWait': 'cmd_dummy',
    'mouseUpRightAt': 'cmd_dummy',
    'mouseUpRightAtAndWait': 'cmd_dummy',
    'open': 'cmd_open',
    'openWindow': 'cmd_dummy',
    'openWindowAndWait': 'cmd_dummy',
    'pause': 'cmd_pause',
    'refresh': 'cmd_refresh',
    'refreshAndWait': 'cmd_refresh',
    'removeAllSelections': 'cmd_dummy',
    'removeAllSelectionsAndWait': 'cmd_dummy',
    'removeScript': 'cmd_dummy',
    'removeScriptAndWait': 'cmd_dummy',
    'removeSelection': 'cmd_dummy',
    'removeSelectionAndWait': 'cmd_dummy',
    'rollup': 'cmd_dummy',
    'rollupAndWait': 'cmd_dummy',
    'runScript': 'cmd_dummy',
    'runScriptAndWait': 'cmd_dummy',
    'select': 'cmd_set',
    'selectAndWait': 'cmd_set',
    'selectFrame': 'cmd_dummy',
    'selectPopUp': 'cmd_dummy',
    'selectPopUpAndWait': 'cmd_dummy',
    'selectWindow': 'cmd_dummy',
    'sendKeys': 'cmd_set',
    'sendKeysAndWait': 'cmd_set',
    'setBrowserLogLevel': 'cmd_dummy',
    'setBrowserLogLevelAndWait': 'cmd_dummy',
    'setCursorPosition': 'cmd_dummy',
    'setCursorPositionAndWait': 'cmd_dummy',
    'setMouseSpeed': 'cmd_dummy',
    'setMouseSpeedAndWait': 'cmd_dummy',
    'setSpeed': 'cmd_dummy',
    'setSpeedAndWait': 'cmd_dummy',
    'setTimeout': 'cmd_dummy',
    'shiftKeyDown': 'cmd_dummy',
    'shiftKeyDownAndWait': 'cmd_dummy',
    'shiftKeyUp': 'cmd_dummy',
    'shiftKeyUpAndWait': 'cmd_dummy',
    'store': 'cmd_store',
    'storeAlert': 'cmd_store',
    'storeAlertPresent': 'cmd_store',
    'storeAllButtons': 'cmd_dummy',
    'storeAllFields': 'cmd_dummy',
    'storeAllLinks': 'cmd_dummy',
    'storeAllWindowIds': 'cmd_dummy',
    'storeAllWindowNames': 'cmd_dummy',
    'storeAllWindowTitles': 'cmd_dummy',
    'storeAttribute': 'cmd_store',
    'storeAttributeFromAllWindows': 'cmd_dummy',
    'storeBodyText': 'cmd_store',
    'storeChecked': 'cmd_store',
    'storeConfirmation': 'cmd_store',
    'storeConfirmationPresent': 'cmd_store',
    'storeCookie': 'cmd_dummy',
    'storeCookieByName': 'cmd_dummy',
    'storeCookiePresent': 'cmd_dummy',
    'storeCursorPosition': 'cmd_dummy',
    'storeEditable': 'cmd_dummy',
    'storeElementHeight': 'cmd_dummy',
    'storeElementIndex': 'cmd_dummy',
    'storeElementPositionLeft': 'cmd_dummy',
    'storeElementPositionTop': 'cmd_dummy',
    'storeElementPresent': 'cmd_store',
    'storeElementWidth': 'cmd_dummy',
    'storeEval': 'cmd_dummy',
    'storeExpression': 'cmd_dummy',
    'storeHtmlSource': 'cmd_dummy',
    'storeLocation': 'cmd_store',
    'storeMouseSpeed': 'cmd_dummy',
    'storeOrdered': 'cmd_dummy',
    'storePrompt': 'cmd_dummy',
    'storePromptPresent': 'cmd_dummy',
    'storeSelectOptions': 'cmd_dummy',
    'storeSelectedId': 'cmd_dummy',
    'storeSelectedIds': 'cmd_dummy',
    'storeSelectedIndex': 'cmd_dummy',
    'storeSelectedIndexes': 'cmd_dummy',
    'storeSelectedLabel': 'cmd_dummy',
    'storeSelectedLabels': 'cmd_dummy',
    'storeSelectedValue': 'cmd_dummy',
    'storeSelectedValues': 'cmd_dummy',
    'storeSomethingSelected': 'cmd_dummy',
    'storeSpeed': 'cmd_dummy',
    'storeTable': 'cmd_dummy',
    'storeText': 'cmd_store',
    'storeTextPresent': 'cmd_dummy',
    'storeTitle': 'cmd_store',
    'storeValue': 'cmd_store',
    'storeVisible': 'cmd_store',
    'storeWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'storeWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'storeXpathCount': 'cmd_store',
    'submit': 'cmd_set',
    'submitAndWait': 'cmd_set',
    'type': 'cmd_set',
    'typeAndWait': 'cmd_set',
    'typeKeys': 'cmd_dummy',
    'typeKeysAndWait': 'cmd_dummy',
    'uncheck': 'cmd_set',
    'uncheckAndWait': 'cmd_set',
    'useXpathLibrary': 'cmd_dummy',
    'useXpathLibraryAndWait': 'cmd_dummy',
    'verifyAlert': 'cmd_alert',
    'verifyAlertNotPresent': 'cmd_alert',
    'verifyAlertPresent': 'cmd_alert',
    'verifyAllButtons': 'cmd_dummy',
    'verifyAllFields': 'cmd_dummy',
    'verifyAllLinks': 'cmd_dummy',
    'verifyAllWindowIds': 'cmd_dummy',
    'verifyAllWindowNames': 'cmd_dummy',
    'verifyAllWindowTitles': 'cmd_dummy',
    'verifyAttribute': 'cmd_verify',
    'verifyAttributeFromAllWindows': 'cmd_dummy',
    'verifyBodyText': 'cmd_verify',
    'verifyChecked': 'cmd_verify',
    'verifyConfirmation': 'cmd_alert',
    'verifyConfirmationNotPresent': 'cmd_alert',
    'verifyConfirmationPresent': 'cmd_alert',
    'verifyCookie': 'cmd_dummy',
    'verifyCookieByName': 'cmd_dummy',
    'verifyCookieNotPresent': 'cmd_dummy',
    'verifyCookiePresent': 'cmd_dummy',
    'verifyCursorPosition': 'cmd_dummy',
    'verifyEditable': 'cmd_dummy',
    'verifyElementHeight': 'cmd_dummy',
    'verifyElementIndex': 'cmd_dummy',
    'verifyElementNotPresent': 'cmd_verify',
    'verifyElementPositionLeft': 'cmd_dummy',
    'verifyElementPositionTop': 'cmd_dummy',
    'verifyElementPresent': 'cmd_verify',
    'verifyElementWidth': 'cmd_dummy',
    'verifyEval': 'cmd_dummy',
    'verifyExpression': 'cmd_dummy',
    'verifyHtmlSource': 'cmd_dummy',
    'verifyLocation': 'cmd_verify',
    'verifyMouseSpeed': 'cmd_dummy',
    'verifyNotAlert': 'cmd_alert',
    'verifyNotAllButtons': 'cmd_dummy',
    'verifyNotAllFields': 'cmd_dummy',
    'verifyNotAllLinks': 'cmd_dummy',
    'verifyNotAllWindowIds': 'cmd_dummy',
    'verifyNotAllWindowNames': 'cmd_dummy',
    'verifyNotAllWindowTitles': 'cmd_dummy',
    'verifyNotAttribute': 'cmd_verify',
    'verifyNotAttributeFromAllWindows': 'cmd_dummy',
    'verifyNotBodyText': 'cmd_verify',
    'verifyNotChecked': 'cmd_verify',
    'verifyNotConfirmation': 'cmd_alert',
    'verifyNotCookie': 'cmd_dummy',
    'verifyNotCookieByName': 'cmd_dummy',
    'verifyNotCursorPosition': 'cmd_dummy',
    'verifyNotEditable': 'cmd_dummy',
    'verifyNotElementHeight': 'cmd_dummy',
    'verifyNotElementIndex': 'cmd_dummy',
    'verifyNotElementPositionLeft': 'cmd_dummy',
    'verifyNotElementPositionTop': 'cmd_dummy',
    'verifyNotElementWidth': 'cmd_dummy',
    'verifyNotEval': 'cmd_dummy',
    'verifyNotExpression': 'cmd_dummy',
    'verifyNotHtmlSource': 'cmd_dummy',
    'verifyNotLocation': 'cmd_verify',
    'verifyNotMouseSpeed': 'cmd_dummy',
    'verifyNotOrdered': 'cmd_dummy',
    'verifyNotPrompt': 'cmd_dummy',
    'verifyNotSelectOptions': 'cmd_dummy',
    'verifyNotSelectedId': 'cmd_dummy',
    'verifyNotSelectedIds': 'cmd_dummy',
    'verifyNotSelectedIndex': 'cmd_dummy',
    'verifyNotSelectedIndexes': 'cmd_dummy',
    'verifyNotSelectedLabel': 'cmd_dummy',
    'verifyNotSelectedLabels': 'cmd_dummy',
    'verifyNotSelectedValue': 'cmd_dummy',
    'verifyNotSelectedValues': 'cmd_dummy',
    'verifyNotSomethingSelected': 'cmd_dummy',
    'verifyNotSpeed': 'cmd_dummy',
    'verifyNotTable': 'cmd_dummy',
    'verifyNotText': 'cmd_verify',
    'verifyNotTitle': 'cmd_verify',
    'verifyNotValue': 'cmd_verify',
    'verifyNotVisible': 'cmd_verify',
    'verifyNotWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'verifyNotWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'verifyNotXpathCount': 'cmd_verify',
    'verifyOrdered': 'cmd_dummy',
    'verifyPrompt': 'cmd_dummy',
    'verifyPromptNotPresent': 'cmd_dummy',
    'verifyPromptPresent': 'cmd_dummy',
    'verifySelectOptions': 'cmd_dummy',
    'verifySelectedId': 'cmd_dummy',
    'verifySelectedIds': 'cmd_dummy',
    'verifySelectedIndex': 'cmd_dummy',
    'verifySelectedLabel': 'cmd_dummy',
    'verifySelectedLabels': 'cmd_dummy',
    'verifySelectedValue': 'cmd_dummy',
    'verifySelectedValues': 'cmd_dummy',
    'verifySomethingSelected': 'cmd_dummy',
    'verifySpeed': 'cmd_dummy',
    'verifyTable': 'cmd_dummy',
    'verifyText': 'cmd_verify',
    'verifyTextNotPresent': 'cmd_dummy',
    'verifyTextPresent ': 'cmd_dummy',
    'verifyTitle': 'cmd_verify',
    'verifyValue': 'cmd_verify',
    'verifyVisible': 'cmd_verify',
    'verifyWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'verifyWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'verifyXpathCount': 'cmd_verify',
    'waitForAlert': 'cmd_wait',
    'waitForAlertNotPresent': 'cmd_wait',
    'waitForAlertPresent': 'cmd_wait',
    'waitForAllButtons': 'cmd_dummy',
    'waitForAllFields': 'cmd_dummy',
    'waitForAllLinks': 'cmd_dummy',
    'waitForAllWindowIds': 'cmd_dummy',
    'waitForAllWindowNames': 'cmd_dummy',
    'waitForAllWindowTitles': 'cmd_dummy',
    'waitForAttribute': 'cmd_wait',
    'waitForAttributeFromAllWindows': 'cmd_dummy',
    'waitForBodyText': 'cmd_wait',
    'waitForChecked': 'cmd_wait',
    'waitForCondition': 'cmd_dummy',
    'waitForConfirmation': 'cmd_wait',
    'waitForConfirmationNotPresent': 'cmd_wait',
    'waitForConfirmationPresent': 'cmd_wait',
    'waitForCookie': 'cmd_dummy',
    'waitForCookieByName': 'cmd_dummy',
    'waitForCookieNotPresent': 'cmd_dummy',
    'waitForCookiePresent': 'cmd_dummy',
    'waitForCursorPosition': 'cmd_dummy',
    'waitForEditable': 'cmd_dummy',
    'waitForElementHeight': 'cmd_dummy',
    'waitForElementIndex': 'cmd_dummy',
    'waitForElementNotPresent': 'cmd_wait',
    'waitForElementPositionLeft': 'cmd_dummy',
    'waitForElementPositionTop': 'cmd_dummy',
    'waitForElementPresent': 'cmd_wait',
    'waitForElementWidth': 'cmd_dummy',
    'waitForEval': 'cmd_dummy',
    'waitForExpression': 'cmd_dummy',
    'waitForFrameToLoad': 'cmd_dummy',
    'waitForHtmlSource': 'cmd_dummy',
    'waitForLocation': 'cmd_wait',
    'waitForMouseSpeed': 'cmd_dummy',
    'waitForNotAlert': 'cmd_wait',
    'waitForNotAllButtons': 'cmd_dummy',
    'waitForNotAllFields': 'cmd_dummy',
    'waitForNotAllLinks': 'cmd_dummy',
    'waitForNotAllWindowIds': 'cmd_dummy',
    'waitForNotAllWindowNames': 'cmd_dummy',
    'waitForNotAllWindowTitles': 'cmd_dummy',
    'waitForNotAttribute': 'cmd_wait',
    'waitForNotAttributeFromAllWindows': 'cmd_dummy',
    'waitForNotBodyText': 'cmd_wait',
    'waitForNotChecked': 'cmd_wait',
    'waitForNotConfirmation': 'cmd_wait',
    'waitForNotCookie': 'cmd_dummy',
    'waitForNotCookieByName': 'cmd_dummy',
    'waitForNotCursorPosition': 'cmd_dummy',
    'waitForNotEditable': 'cmd_dummy',
    'waitForNotElementHeight': 'cmd_dummy',
    'waitForNotElementIndex': 'cmd_dummy',
    'waitForNotElementPositionLeft': 'cmd_dummy',
    'waitForNotElementPositionTop': 'cmd_dummy',
    'waitForNotElementWidth': 'cmd_dummy',
    'waitForNotEval': 'cmd_dummy',
    'waitForNotExpression': 'cmd_dummy',
    'waitForNotHtmlSource': 'cmd_dummy',
    'waitForNotLocation': 'cmd_wait',
    'waitForNotMouseSpeed': 'cmd_dummy',
    'waitForNotOrdered': 'cmd_dummy',
    'waitForNotPrompt': 'cmd_dummy',
    'waitForNotSelectOptions': 'cmd_dummy',
    'waitForNotSelectedId': 'cmd_dummy',
    'waitForNotSelectedIds': 'cmd_dummy',
    'waitForNotSelectedIndex': 'cmd_dummy',
    'waitForNotSelectedIndexes': 'cmd_dummy',
    'waitForNotSelectedLabel': 'cmd_dummy',
    'waitForNotSelectedLabels': 'cmd_dummy',
    'waitForNotSelectedValue': 'cmd_dummy',
    'waitForNotSelectedValues': 'cmd_dummy',
    'waitForNotSomethingSelected': 'cmd_dummy',
    'waitForNotSpeed': 'cmd_dummy',
    'waitForNotTable': 'cmd_dummy',
    'waitForNotText': 'cmd_wait',
    'waitForNotTitle': 'cmd_wait',
    'waitForNotValue': 'cmd_wait',
    'waitForNotVisible': 'cmd_wait',
    'waitForNotWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'waitForNotWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'waitForNotXpathCount': 'cmd_wait',
    'waitForOrdered': 'cmd_dummy',
    'waitForPageToLoad': 'cmd_dummy',
    'waitForPopUp': 'cmd_dummy',
    'waitForPrompt': 'cmd_dummy',
    'waitForPromptNotPresent': 'cmd_dummy',
    'waitForPromptPresent': 'cmd_dummy',
    'waitForSelectOptions': 'cmd_dummy',
    'waitForSelectedId': 'cmd_dummy',
    'waitForSelectedIds': 'cmd_dummy',
    'waitForSelectedIndex': 'cmd_dummy',
    'waitForSelectedIndexes': 'cmd_dummy',
    'waitForSelectedLabel': 'cmd_dummy',
    'waitForSelectedLabels': 'cmd_dummy',
    'waitForSelectedValue': 'cmd_dummy',
    'waitForSelectedValues': 'cmd_dummy',
    'waitForSomethingSelected': 'cmd_dummy',
    'waitForSpeed': 'cmd_dummy',
    'waitForTable': 'cmd_dummy',
    'waitForText': 'cmd_wait',
    'waitForTextNotPresent': 'cmd_dummy',
    'waitForTextPresent': 'cmd_dummy',
    'waitForTitle': 'cmd_wait',
    'waitForValue': 'cmd_wait',
    'waitForVisible': 'cmd_wait',
    'waitForWhetherThisFrameMatchFrameExpression': 'cmd_dummy',
    'waitForWhetherThisWindowMatchWindowExpression': 'cmd_dummy',
    'waitForXpathCount': 'cmd_wait',
    'windowFocus': 'cmd_dummy',
    'windowFocusAndWait': 'cmd_dummy',
    'windowMaximize': 'cmd_dummy',
    'windowMaximizeAndWait': 'cmd_dummy'
}
