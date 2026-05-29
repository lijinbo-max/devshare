import { ref, onMounted, watch, computed } from 'vue'
import { StorageKeys } from '../utils'

export type ThemeMode = 'light' | 'dark' | 'system'

export type ResolvedTheme = 'light' | 'dark'

export const useTheme = () => {
  const themeMode = ref<ThemeMode>('system')
  const systemTheme = ref<ResolvedTheme>(
    window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  )
  const hasUserPreference = ref(false)

  const currentTheme = computed<ResolvedTheme>(() => {
    if (themeMode.value === 'system') {
      return systemTheme.value
    }
    return themeMode.value
  })

  const applyTheme = (newTheme: ResolvedTheme) => {
    document.documentElement.setAttribute('data-theme', newTheme)
  }

  const toggleTheme = () => {
    const modes: ThemeMode[] = ['light', 'dark', 'system']
    const currentIndex = modes.indexOf(themeMode.value)
    themeMode.value = modes[(currentIndex + 1) % modes.length]
    hasUserPreference.value = themeMode.value !== 'system'
    
    try {
      sessionStorage.setItem(StorageKeys.THEME, themeMode.value)
      localStorage.setItem(StorageKeys.THEME, themeMode.value)
      sessionStorage.setItem('hasUserPreference', String(hasUserPreference.value))
      localStorage.setItem('hasUserPreference', String(hasUserPreference.value))
    } catch (e) {
      console.log('Storage not available')
    }
    
    applyTheme(currentTheme.value)
  }

  const setTheme = (newTheme: ThemeMode) => {
    themeMode.value = newTheme
    hasUserPreference.value = newTheme !== 'system'
    
    try {
      sessionStorage.setItem(StorageKeys.THEME, newTheme)
      localStorage.setItem(StorageKeys.THEME, newTheme)
      sessionStorage.setItem('hasUserPreference', String(hasUserPreference.value))
      localStorage.setItem('hasUserPreference', String(hasUserPreference.value))
    } catch (e) {
      console.log('Storage not available')
    }
    
    applyTheme(currentTheme.value)
  }

  watch(currentTheme, (newTheme) => {
    applyTheme(newTheme)
  })

  onMounted(() => {
    let savedHasPreference = false
    
    try {
      savedHasPreference = sessionStorage.getItem('hasUserPreference') === 'true'
    } catch (e) {}
    
    if (!savedHasPreference) {
      try {
        savedHasPreference = localStorage.getItem('hasUserPreference') === 'true'
      } catch (e) {}
    }
    
    hasUserPreference.value = savedHasPreference
    
    let savedTheme: ThemeMode | null = null
    
    try {
      savedTheme = sessionStorage.getItem(StorageKeys.THEME) as ThemeMode | null
    } catch (e) {}
    
    if (!savedTheme) {
      try {
        savedTheme = localStorage.getItem(StorageKeys.THEME) as ThemeMode | null
      } catch (e) {}
    }
    
    if (savedTheme && (savedTheme === 'light' || savedTheme === 'dark')) {
      themeMode.value = savedTheme
    } else if (savedHasPreference) {
      themeMode.value = 'light'
    } else {
      themeMode.value = 'system'
    }

    applyTheme(currentTheme.value)

    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
    
    const handleSystemChange = (e: MediaQueryListEvent) => {
      systemTheme.value = e.matches ? 'dark' : 'light'
    }

    mediaQuery.addEventListener('change', (e) => {
      if (themeMode.value === 'system') {
        handleSystemChange(e)
      }
    })

    return () => {
      mediaQuery.removeEventListener('change', handleSystemChange)
    }
  })

  return {
    themeMode,
    currentTheme,
    toggleTheme,
    setTheme
  }
}
